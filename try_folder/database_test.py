
import database as db
tmp = db.riddle_db("try.db")
tmp.add_riddle("a","1")
tmp.add_riddle("b","t")
tmp.add_riddle("c","3")
tmp.add_riddle("d","4")

a= tmp.get_answer_by_riddle("c")
print(a)

b= tmp.get_answer_by_number_id(1)
print(b)
