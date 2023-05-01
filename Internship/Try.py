def f3():
    mw.withdraw()
    vw.deiconify()
    vw_st_data.delete(1.0, END)
    con = None
    try:
        con = connect("er.db")
        cursor = con.cursor()
        sql = "select * from employee"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info = info + " ID " + str(d[0]) + " Name = " + str(d[1]) + " Salary = " + str(d[2]) + "\n"
        vw_st_data.insert(INSERT, info)
    except Exception as e:
        showerror("issue ", e)
    finally:
        if con is not None:
            con.close()

