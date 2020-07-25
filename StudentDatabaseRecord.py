import sqlite3

def studentResult():
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS studentRecord(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, CourseCode text, CN text, TOC text, SDL text, ISEE text, SEPM text, DBMS text, PracCN text, PracDBMS text, TotalScore text, Average text, Ranking text)")
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Surname, CourseCode, CN, TOC, SDL, ISEE, SEPM, DBMS, PracCN, PracDBMS, TotalScore, Average, Ranking):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("INSERT INTO studentRecord VALUES (null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(StdID, Firstname, Surname, CourseCode, CN, TOC, SDL, ISEE, SEPM, DBMS, PracCN, PracDBMS, TotalScore, Average, Ranking))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentRecord")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("DELETE FROM studentRecord WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID="", Firstname="", Surname="", CourseCode="", CN="", TOC="", SDL="", ISEE="", SEPM="", DBMS="", PracCN="", PracDBMS="", TotalScore="", Average="", Ranking=""):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentRecord WHERE StdID=? OR Firstname=? OR Surname=? OR CourseCode=? OR CN=? OR TOC=? OR SDL=? OR ISEE=? OR SEPM=? OR DBMS=? OR PracCN=? OR PracDBMS=? OR TotalScore=? OR Average=? OR Ranking=? ", (StdID, Firstname, Surname, CourseCode, CN, TOC, SDL, ISEE, SEPM, DBMS, PracCN, PracDBMS, TotalScore, Average, Ranking))
    rows = cur.fetchall()
    con.close()
    return rows

def updateData(StdID="", Firstname="", Surname="", CourseCode="", CN="", TOC="", SDL="", ISEE="", SEPM="", DBMS="", PracCN="", PracDBMS="", TotalScore="", Average="", Ranking=""):
    con = sqlite3.connect("studentRecord.db")
    cur = con.cursor()
    cur.execute("UPDATE studentRecord SET StdID=? OR Firstname=? OR Surname=? OR CourseCode=? OR CN=? OR TOC=? OR SDL=? OR ISEE=? OR SEPM=? OR DBMS=? OR PracCN=? OR PracDBMS=? OR TotalScore=? OR Average=? OR Ranking=? ", (StdID, Firstname, Surname, CourseCode, CN, TOC, SDL, ISEE, SEPM, DBMS, PracCN, PracDBMS, TotalScore, Average, Ranking))
    con.commit()
    con.close()

studentResult()