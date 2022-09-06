from flask_restful import Resource, reqparse
from app.lib.notifications import PushNote as PushN
from app.lib.notifications import PushLink as PushL

PushNot_parser = reqparse.RequestParser()
PushNot_parser.add_argument('title', required=True, help= 'missing title')
PushNot_parser.add_argument('body', required=True, help= ' missing body')
PushNot_parser.add_argument('api_key', required=True, help= ' missing api_key')


class PushNote(Resource):
    def post(self):
        args = PushNot_parser.parse_args()

        try:
            PushN(args['title'], args['body'], args['api_key'])
            return {'message':'success'}
        except:
            return {'message':'Could not push notification check api_key if valid'}


PushLink_parser = reqparse.RequestParser()
PushLink_parser.add_argument('title', required=True, help= 'missing title')
PushLink_parser.add_argument('body', required=True, help= ' missing body')
PushLink_parser.add_argument('url', required=True, help= ' missing url')
PushLink_parser.add_argument('api_key', required=True, help= ' missing api_key')
class PushLink(Resource):
    def post(self):
        args = PushLink_parser.parse_args()

        try:
            PushL(args['title'], args['body'],args['url'], args['api_key'])
            return {'message':'success'}
        except:
            return {'message':'Could not push notification check api_key if valid'}

        
