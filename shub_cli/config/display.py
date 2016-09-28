from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

error_style = style_from_dict({
    Token.ErrorMessage: '#ff0066',
    Token.ShubFileModel: '#ccaa33',
    Token.NoInternetConnection: '#ff0066',
})

shub_not_configured_tokens = [
    (Token.ErrorMessage, 'You need to set up your .scrapinghub.yml with a default project and api key:\n'),
    (Token.ShubFileModel,
     '''
     ~/.scrapinghub.yml

     apikeys:
       default: v65a787a987k08k9s797d7s8l98298sw
     projects:
       default: 89090
     '''
     ),
]

no_internet_connection_tokens = [
    (Token.NoInternetConnection, 'You do not have Internet connection.')
]

TABLE_JOB_MODEL = [['Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']]

TABLE_JOBS_MODEL = [['Id', 'Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']]
