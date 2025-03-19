# from lib.database_connection import get_flask_database_connection
# from lib.drill_respository import DrillRepository
# from lib.drill import Drill
# from flask import request

# # You won't need to nest your routes in app.py in a method like this
# def apply_example_routes(app):
#     # GET /drills
#     # Returns a list of drills
#     # Try it:
#     #   ; curl http://localhost:5001/drills
#     @app.route('/drills', methods=['GET'])
#     def get_drills():
#         connection = get_flask_database_connection(app)
#         repository = DrillRepository(connection)
#         return "\n".join([
#             str(drill) for drill in repository.all()
#         ])


#     # GET /drills/<id>
#     # Returns a single drill
#     # Try it:
#     #   ; curl http://localhost:5001/drills/1
#     @app.route('/drills/<int:id>', methods=['GET'])
#     def get_drill(id):
#         connection = get_flask_database_connection(app)
#         repository = DrillRepository(connection)
#         return str(repository.find(id))


#     # POST /drills
#     # Creates a new drill
#     # Try it:
#     #   ; curl -X POST -d "title=Dave&author_name=Caden%20Lovelace" http://localhost:5001/drills
#     @app.route('/drills', methods=['POST'])
#     def create_drill():
#         connection = get_flask_database_connection(app)
#         repository = DrillRepository(connection)
#         drill = Drill(None, request.form['drill_name'], request.form['drill_type'])
#         drill = repository.create(drill)
#         return "Drill added successfully"


#     # # DELETE /books/<id>
#     # # Deletes a book
#     # # Try it:
#     # #   ; curl -X DELETE http://localhost:5001/books/1
#     # @app.route('/books/<int:id>', methods=['DELETE'])
#     # def delete_book(id):
#     #     connection = get_flask_database_connection(app)
#     #     repository = BookRepository(connection)
#     #     repository.delete(id)
#     #     return "Book deleted successfully"
