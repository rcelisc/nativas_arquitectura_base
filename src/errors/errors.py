
class ApiError(Exception):
    code = 422
    description = "Default message"

class  InvalidParams(ApiError):
	code  =  400
	description  =  "Bad param"