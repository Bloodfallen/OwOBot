commandSyntax = "$o" # What syntax should be used to call upon the bot?
NSFW = False # Allow the bot to post NSFW content?
EnhancedLogging = True # Enable enhanced logging? (Defined below)

#
#   Enhanced logging allows for logging extra information to the console, this could be any of the following,
#   but is not limited to it.
#
#   When someone requests an image, and what that image is.
#   When someone attempts to use an Admin-Only command without proper authorization
#   The ID, reason, and length of a user ban (future)
#
#   The bot DOES NOT, unless explicitly specified, log the following
#
#   User ID's
#   User names
#   User#ID
#   Email addresses
#   Profile pictures
#   Profile backgrounds
#   User content
#
#   When a user is issued a ban, or warning, the following content will be logged to both text file and console output.
#
#   User#ID
#   Reasoning for the ban
#   Length of the ban
#   