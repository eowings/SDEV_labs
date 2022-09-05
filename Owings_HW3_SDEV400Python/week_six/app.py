"""
| __filename__ = "app.py" (for week_six)
| __coursename__ = "SDEV 400 - Secure Programming in the Cloud"
| __author__ = "Eddy Owings"
| __copyright__ = "Craig Poma"
| __credits__ = ["Craig Poma"]
| __license__ = "MIT"
| __version__ = "1.0.0"
| __maintainer__ = "Eddy Owings"
| __email__ = "eowings@student.umgc.edu"
| __status__ = "Baseline"
| __docformat__ = 'reStructuredText'

"""

import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from flask import Flask, request, json


##########################################
# Create APP for handling API/REST Calls
##########################################
app = Flask(__name__)

########################################
# DATA Set mapper for input JSON files
########################################
DATA_SET_MAPPER = {
    'SPORTS': 'combined_scores.json',
}

####################################################################
# Defined deployment stage for API Gateway
####################################################################
API_GATEWAY_STAGE = ''
if 'API_GATEWAY_STAGE' in os.environ and os.environ['API_GATEWAY_STAGE'] is not None:
    API_GATEWAY_STAGE = os.environ['API_GATEWAY_STAGE']

################################################
# Return non-JSON formatted results for scores?
################################################
PRETTY_RESPONSE = False

####################################################################
# Defined Pretty Text Warning
####################################################################
PRETTY_WARNING = "\r\n\r\nTHIS IS NOT JSON - IT IS PRETTY TEXT FOR FORMATTING BECAUSE"\
                 + " YOU PASSED IN URL var &pretty_response=1 \r\n\r\n\r\n"

####################################################################
# Define current path of Python Application for output/input files
# Does not work properly within LAMBDA for a valid path, but for local
# test it is useful to have the path.
####################################################################
CURRENT_SCRIPT_PATH = os.path.dirname(sys.argv[0])

####################################################
# Is this application running in REST API ONLY mode
####################################################
REST_API_ONLY_MODE = False

####################################
# Are VALIDATORS for inputs active?
####################################
VALIDATORS = True

####################################################################
# Catch Exceptions and write them to log file in current folder.
####################################################################
LOG_FILE = Path(CURRENT_SCRIPT_PATH + '/' + 'messages.log')
logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s %(levelname)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w', # Overwrite the log file
                    level=logging.INFO)
# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
#####################################################################

def get_site_base():
    """ Build dynamic site base URL """

    request_url = urlparse(request.base_url)
    host = request_url.hostname
    port = request_url.port
    http = "http://"
    if port == 80:
        port = ""
    elif port == 443:
        http = "https://"
        port = ""
    elif port is None:
        port = ""
    else:
        port = ":" + str(port)

    return "{}{}{}/{}".format(http, host, port, API_GATEWAY_STAGE)

def validate_name(selection=None):
    """
    Capture and Validate Name meets naming requirement

    :param selection(str): Value string to validate
    :rtype: **bool**
    :return: **valid_input(str)**: Name (First or Last) validated to match \
    A-Z, a-z, and -. Must be DNS compliant so, apostrophe (') not treated as a \
    valid name character (i.e. O'Brian will not work - it isn't DNS compliant).\
    ) for false and 1 for True will be returned
    """

    valid_input = 0
    # Handle A-Z a-z and - in name
    if re.fullmatch('^[a-z A-Z]+(-[a-z A-Z]+)?$', selection):
        valid_input = 1

    return valid_input


def read_dataset_from_file(input_file=None):
    """
    Read Data from JSON file.

    :param input_file(str): Input file name
    :rtype: **dict**
    :return: **json_data(dict)**: DICT of JSON or None
    """

    json_data = None
    try:
        json_file = './data_sets/' + input_file

        # if 'LAMBDA_MODE' in os.environ and os.environ['LAMBDA_MODE'] == 1:
        #     # We are running in LAMBDA_MODE mode this gets set via sls deploy
        #     # The serverless.yml is configured to set environment variables.
        #     #
        #     # functions:
        #     #    app:
        #     #      handler: wsgi_handler.handler
        #     #      environment:
        #     #        API_GATEWAY_STAGE: dev/
        #     #        LAMBDA_MODE: 1
        #     #
        #     json_file = './data_sets/' + input_file
        # else:
        #     # In LAMBDA the file is in the current directory, but
        #     # in other modes we will have to get the full path
        #     json_file = Path(CURRENT_SCRIPT_PATH + '/data_sets/' + input_file)

        with open(json_file) as json_file:
            json_data = json.load(json_file)

    except FileNotFoundError as file_exception:
        _ = generic_output_msg(log_message="Error with JSON. File Exception was: {}"\
                              .format(str(file_exception)))
        json_data = {'ERROR': {
            'STATUS': 'ERROR',
            'MESSAGE': "Error with JSON. File Exception was: {}"\
            .format(str(file_exception)),
        }}

    return json_data

def generic_output_msg(log_message=None, print_to_screen=True, exit_app=False):
    """
    Write log to file and screen/console.

    :param log_message(str): String to output to logs file and screen/console
    :param print_to_screen(bool): Output message to screen
    :rtype: **None**
    :return: **None**
    """

    print_message = ""
    if log_message is not None:
        logging.info("".join(log_message.splitlines()))
        print_message = "\r\n" + '*' * 100 + "\r\n" + log_message + "\r\n" + '*' * 100
        if print_to_screen and REST_API_ONLY_MODE is not True:
            print(print_message)
        else:
            print_message = log_message
        if exit_app:
            sys.exit()
    return print_message


@app.route("/week_six_help")
def week_six_help():
    """
    API Query Help.

    :rtype: **app.response_class**
    :return: **response(app.response_class)**: Encoded response with full API help/documentation
    """
    pretty_response = PRETTY_RESPONSE
    argv_val_pretty = request.args.get('pretty_response')
    join_val = " "
    if argv_val_pretty is not None:
        if argv_val_pretty.lower() in ('1', 'true'):
            pretty_response = True
            join_val = "\r\n"

    # C0301: Line too long (103/100) (line-too-long)
    # pylint: disable=C0301
    site_url = get_site_base()
    message = [
                "The Week Six API works off a GET query string. Expected parts are:",
                "sport_type and team_abbr.",
                "To see a list of sport teams:",
                " ",
                "FOOTBALL TEAMS LIST:",
                "{}football_list?pretty_response=1".format(site_url),
                "BASEBALL TEAMS LIST:",
                "{}baseball_list?pretty_response=1".format(site_url),
                "NCAAF TEAMS LIST:",
                "{}ncaaf_list?pretty_response=1".format(site_url),
                " ",
                "Try these sample URLs to get yourself started:{}".format(join_val),
                "SOME EXAMPLE QUERIES{}".format(join_val),
                "Check how the Chiefs did: {}?sport_type=football&team_abbr=kan&pretty_response=1 {}".format(site_url, join_val),
                "Check how the Royals did: {}?sport_type=baseball&team_abbr=kcr&pretty_response=1 {}".format(site_url, join_val),
                "Check how Missouri did: {}?sport_type=ncaaf&team_abbr=missouri&pretty_response=1 {}".format(site_url, join_val),
    ]
    # pylint: enable=C0301

    data = join_val.join(message)
    if pretty_response is True:
        pretty_warning = PRETTY_WARNING
        response = app.response_class(
            response=pretty_warning + data,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )

    return response

@app.route('/ncaaf_list')
def ncaaf_list():
    """
    List known ncaaf teams.
    """

    data_set = 'SPORTS'
    pretty_response = PRETTY_RESPONSE
    argv_val_pretty = request.args.get('pretty_response')
    join_val = " "
    if argv_val_pretty is not None:
        if argv_val_pretty.lower() in ('1', 'true'):
            pretty_response = True
            join_val = "\r\n"

    argv_val_dataset = request.args.get('dataset')
    if argv_val_dataset is not None:
        if argv_val_pretty.upper() in DATA_SET_MAPPER:
            data_set = argv_val_dataset

    list_ncaaf = read_dataset_from_file(input_file=DATA_SET_MAPPER[data_set])

    if 'ERROR' in list_ncaaf:
        data = list_ncaaf['ERROR']['MESSAGE']
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )
        return response

    cfb_list = []
    # for a_staffer in hello_list['STAFF']:
    for a_team in list_ncaaf['ncaaf']:
        cfb_list.append("({}) {}".format(a_team['away_abbr'], a_team['away_name']))
        cfb_list.append("({}) {}".format(a_team['home_abbr'], a_team['home_name']))
        cfb_list = sorted(list(set(cfb_list)))

    data = join_val.join(cfb_list)
    if pretty_response is True:
        pretty_warning = PRETTY_WARNING
        response = app.response_class(
            response=pretty_warning + data,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )

    return response

@app.route('/baseball_list')
def baseball_list():
    """
    List known baseball teams.
    """

    data_set = 'SPORTS'
    pretty_response = PRETTY_RESPONSE
    argv_val_pretty = request.args.get('pretty_response')
    join_val = " "
    if argv_val_pretty is not None:
        if argv_val_pretty.lower() in ('1', 'true'):
            pretty_response = True
            join_val = "\r\n"

    argv_val_dataset = request.args.get('dataset')
    if argv_val_dataset is not None:
        if argv_val_pretty.upper() in DATA_SET_MAPPER:
            data_set = argv_val_dataset

    list_baseball = read_dataset_from_file(input_file=DATA_SET_MAPPER[data_set])

    if 'ERROR' in list_baseball:
        data = list_baseball['ERROR']['MESSAGE']
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )
        return response

    bb_list = []
    # for a_staffer in hello_list['STAFF']:
    for a_team in list_baseball['baseball']:
        bb_list.append("({}) {}".format(a_team['away_abbr'], a_team['away_name']))
        bb_list = sorted(list(set(bb_list)))

    data = join_val.join(bb_list)
    if pretty_response is True:
        pretty_warning = PRETTY_WARNING
        response = app.response_class(
            response=pretty_warning + data,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )

    return response

@app.route('/football_list')
def football_list():
    """
    List known football teams.
    """

    data_set = 'SPORTS'
    pretty_response = PRETTY_RESPONSE
    argv_val_pretty = request.args.get('pretty_response')
    join_val = " "
    if argv_val_pretty is not None:
        if argv_val_pretty.lower() in ('1', 'true'):
            pretty_response = True
            join_val = "\r\n"

    argv_val_dataset = request.args.get('dataset')
    if argv_val_dataset is not None:
        if argv_val_pretty.upper() in DATA_SET_MAPPER:
            data_set = argv_val_dataset

    list_football = read_dataset_from_file(input_file=DATA_SET_MAPPER[data_set])

    if 'ERROR' in list_football:
        data = list_football['ERROR']['MESSAGE']
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )
        return response

    fb_list = []
    # for a_staffer in hello_list['STAFF']:
    for a_team in list_football['football']:
        fb_list.append("({}) {}".format(a_team['away_abbr'], a_team['away_name']))
        fb_list = sorted(list(set(fb_list)))

    data = join_val.join(fb_list)
    if pretty_response is True:
        pretty_warning = PRETTY_WARNING
        response = app.response_class(
            response=pretty_warning + data,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )

    return response

@app.route("/")
def week_six():
    """ Amazon Lambda and API Gateway - week_six"""

    data_set = 'SPORTS'
    pretty_response = PRETTY_RESPONSE
    argv_val_pretty = request.args.get('pretty_response')
    join_val = " "
    if argv_val_pretty is not None:
        if argv_val_pretty.lower() in ('1', 'true'):
            pretty_response = True
            join_val = "\r\n"

    argv_val_dataset = request.args.get('dataset')
    if argv_val_dataset is not None:
        if argv_val_pretty.upper() in DATA_SET_MAPPER:
            data_set = argv_val_dataset

    site_url = get_site_base()
    message = [
                "A sport and team abbreviation URL var is required. Please use the Week Six API",
                "{}week_six_help?pretty_response=1 for more information.".format(site_url),
                "Try one of the following sports:",
                "FOOTBALL",
                "BASEBALL",
                "NCAAF",
    ]
    data = {"MESSAGE": " ".join(message)}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')

    if request.args.get('sport_type') is None or request.args.get('team_abbr') is None:
        return response

    if request.args.get('sport_type').lower() != 'football':
        if request.args.get('sport_type').lower() != 'baseball':
            if request.args.get('sport_type').lower() != 'ncaaf':
                return response

    if not validate_name(selection=request.args.get('sport_type')):
        _ = generic_output_msg(log_message="Invalid sport_type {} was provided"\
                              .format(request.args.get('sport_type')))
        return response

    if not validate_name(selection=request.args.get('team_abbr')):
        _ = generic_output_msg(log_message="Invalid team_abbr {} was provided"\
                              .format(request.args.get('team_abbr')))
        return response

    sport_list = ["I can't help you with {} {}, try another team."\
                     .format(request.args.get('sport_type'), request.args.get('team_abbr'))]

    hello_list = read_dataset_from_file(input_file=DATA_SET_MAPPER[data_set])
    if 'ERROR' in hello_list:
        data = hello_list['ERROR']['MESSAGE']
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )
        return response

    sport = request.args.get('sport_type').lower()
    team = request.args.get('team_abbr').lower()

    for a_team in hello_list[sport]:
        if a_team['winning_abbr'].lower() == team\
        or a_team['losing_abbr'].lower() == team:
            sport_list = []

    for a_team in hello_list[sport]:
        if a_team['winning_abbr'].lower() == team\
        or a_team['losing_abbr'].lower() == team:
            sport_list.append("{} beat {} {}/{} on {}".format
                              (a_team['winning_name'],
                               a_team['losing_name'],
                               max(a_team['away_score'], a_team['home_score']),
                               min(a_team['away_score'], a_team['home_score']),
                               change_date_format(a_team['boxscore'])))
            sport_list = list(set(sport_list))
            sport_list = sorted(sport_list, key=lambda x: x.split()[-1])

    data = join_val.join(sport_list)
    if pretty_response is True:
        pretty_warning = PRETTY_WARNING
        response = app.response_class(
            response=pretty_warning + data,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=json.dumps({"MESSAGE": data}),
            mimetype='application/json'
        )

    return response

def change_date_format(date):
    """strips alpha and special chars and changes boxscore date format"""
    string = re.sub('[^0-9]', '', date)
    if len(string) == 9:
        string = string[:-1]
    for fmt in ('%Y%m%d', '%Y%m%d%s', '%d/%m/%Y'):
        try:
            string = datetime.strptime(string, fmt)
            return string.strftime('%m-%d-%Y')
        except ValueError:
            pass
    raise ValueError('no valid date format found')

@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(error):
    """
    Handle gracefully pages not found
    """
    site_url = get_site_base()
    message = [
                "System error {}. Please use the Hello World API".format(error),
                "{}week_six_help?pretty_response=1 for more information.".format(site_url),
    ]
    data = {"MESSAGE": " ".join(message)}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')

    return response

if __name__ == "__main__":
    # Testing in CLOUD9IDE
    app.run(host='0.0.0.0', port=8080, debug=True)
    # Testing locally in PyCharm
    #app.run(host='127.0.0.1', port=8080, debug=True)
