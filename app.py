from flask import Flask, render_template , request,flash,redirect, session,jsonify


from sqlalchemy import create_engine, MetaData, Table, Column, Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base
import sqlalchemy.orm

from datetime import date



e=create_engine('sqlite:///Sitedata.db')
sess=sessionmaker(bind=e)
ses=sess()
meta=MetaData()
base=declarative_base()




class user_personal(base):
    __tablename__='user_personal'
    admno=Column(Integer,primary_key=True,autoincrement=True)
    fname=Column(String(30))
    lname=Column(String(30))
    email=Column(String(60))
    fathername=Column(String(40))
    mothername=Column(String(40))
    address=Column(String(100))
    studentphone=Column(String(10))
    parentphone=Column(String(10))
    bloodgroup=Column(String(2))
    gender=Column(String(6))
    conveyance=Column(String(10))
    dob=Column(String(10))
    passwd=Column(String(40))

class user_academic(base):
    __tablename__='user_academic'
    admno=Column(Integer,primary_key=True,autoincrement=True)
    clas=Column(String(2))
    section=Column(String(1))
    DOA=Column(String(10))
    sub1=Column(String(30))
    sub2=Column(String(30))
    sub3=Column(String(30))
    sub4=Column(String(30))
    sub5=Column(String(30))
    sub6=Column(String(30)) 


class user_fees(base):
    __tablename__='user_fees'
    admno=Column(Integer,primary_key=True,autoincrement=True)
    apr=Column(String(10))
    may=Column(String(10))
    jun=Column(String(10))
    jul=Column(String(10))
    aug=Column(String(10))
    sep=Column(String(10))
    oct=Column(String(10))
    nov=Column(String(10))
    dec=Column(String(10))
    jan=Column(String(10))
    feb=Column(String(10))
    mar=Column(String(10))

class txns(base):
    __tablename__='txns'
    txnid=Column(Integer,primary_key=True,autoincrement=True)
    date=Column(String(10))
    method=Column(String(15))
    paymentid=Column(String(30))
    amt=Column(String(10))



# base.metadata.create_all(e)


# ses.flush()
# ses.add(txns(txnid='240000001'))
# ses.add(user_fees(admno='20240002'))
# ses.add(user_academic(admno='20240002'))
# ses.add(user_personal(admno='20240002'))


# ses.commit()






# print("Start")
# obj=user_personal(admno='20240002',fname='Aryan',lname='Sharma',email="aryansharma0305@gmail.com",fathername='Rajeev',mothername='Ruchi',
#                   address='Bakli Phatak',studentphone='7983981756',parentphone='9410601970',bloodgroup='B+',gender='Male',
#                   conveyance='Self',dob='05/03/2004',passwd="ARYA0001")

# ses.add(obj)
# ses.commit()
# print("End")

    
    





app = Flask(__name__,static_url_path='/Static')


app.config['SECRET_KEY']='%lkyg((t5*65UYf^jGF7$b7HJg4fk2Y22f'


@app.route('/')
def hello_world():
    return render_template("index.html")





@app.route('/about')
def about():
    return (render_template('about.html'))

@app.route('/calculator',methods=["GET","POST"])
def calculator():
    try:
        print('=========head======',"\n")
        print(request.method)
        if request.method=='POST':
            btn=request.form['btn']
            if btn=='clrbtn':
                return (render_template("calculator.html",ans=''))
            num1=(request.form['num1'])
            num2=request.form['num2']
            if num1 != '' and num2 !='':
                num1=int(num1)
                num2=int(num2)
                if btn=="addbtn":
                    ans=num1+num2
                elif btn=='subbtn':
                    ans=num1-num2
                elif btn=='mulbtn':
                    ans=num1*num2
                elif btn=='divbtn':
                    ans=num1/num2     
                ans=str(ans)
                print(request.form)
                return (render_template("calculator.html",ans=ans))
            else:
                print(request.form)
                return (render_template("calculator.html",ans=request.form['output']))     
        else:
            print(request.form) 
            return (render_template("calculator.html",ans=''))
    except:
            return (render_template("calculator.html",ans='ERROR'))        

@app.route('/jee')
def jee():
    return(render_template('jee.html'))

@app.route('/register',methods=["GET","POST"])
def resgiter():
    if request.method=='GET':
        return(render_template('register.html',alert_text=""))
    elif request.method=="POST":
        try:
            fname=str(request.form['f_name'].strip())
            lname=str(request.form['l_name'].strip())
            email=str(request.form['email'].strip())
            passwd1=str(request.form['passwd1'].strip())
            passwd2=str(request.form['passwd2'].strip())
            print(fname,lname,email,passwd1,passwd2)
            
            if fname=="" or lname=="" or email=='' or passwd1=='' or passwd2=='':
                return(render_template('register.html',alert_text="Fields Can Not Be Empty!!"))
            else:    
                if passwd1==passwd2:
                    ses.rollback()
                    entry_obj=user_personal(email=email,fname=fname,lname=lname,passwd=passwd1)
                    ses.add(entry_obj)
                    ses.commit()
                    return(render_template('register.html',alert_text="Account created succesfully!"))
                else:
                    return(render_template('register.html',alert_text="Passwords didn't match !!"))

        except:
            return(render_template('register.html',alert_text="User Already exists"))

        
    else:
        return ("ERROR")        




    







@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="GET":
        return(render_template('login.html',alert_text=""))
    elif request.method=="POST":
        print(request.form)
        admno=request.form['admno'].strip()
        passwd=request.form['passwd'].strip()  
        try:
            result=ses.query(user_personal).filter(user_personal.admno==admno).first()
            if result.passwd==passwd:
                session['logging_status']=True
                session['admno']=admno
                return(redirect('/dashboard'))
            else:
                return(render_template('login.html',alert_text="WRONG PASS!!"))
        except:
            return(render_template('login.html',alert_text="USER DOESNT EXIST !!"))
        
        
        

    else:
        return("ERROR")






@app.route('/dashboard')
def dash():
    if ('logging_status' in session) and ('admno' in session) :
        if session['logging_status']==True:
            admno=session['admno']
            pd=ses.query(user_personal).filter_by(admno=(session['admno'])).first()
            fullname=pd.fname+' '+pd.lname
            return(render_template('dashboard.html',name=fullname))
        else:
            return(redirect('/login'))
    else:
        return(redirect('/login'))




@app.route('/dashboard/profile')
def dash_profile():

    if 'logging_status' in session:
        if session['logging_status']==True:
            pd=ses.query(user_personal).filter_by(admno=(session['admno'])).first()
            ad=ses.query(user_academic).filter_by(admno=(session['admno'])).first()
           
            fname=pd.fname
            lname=pd.lname
            email=pd.email
            fathername=pd.fathername
            mothername=pd.mothername
            address=pd.address
            studentphone=pd.studentphone
            parentphone=pd.parentphone
            bloodgroup=pd.bloodgroup
            gender=pd.gender
            conveyance=pd.conveyance
            dob=pd.dob
            clas=ad.clas
            section=ad.section
            admno=session['admno']
            DOA=ad.DOA
            sub1=ad.sub1
            sub2=ad.sub2
            sub3=ad.sub3
            sub4=ad.sub4
            sub5=ad.sub5
            sub6=ad.sub6
            fd=ses.query(user_fees).filter_by(admno=admno).first()
            feebymonth=[fd.apr,fd.may,fd.jun,fd.jul,fd.aug,fd.sep,fd.oct,fd.nov,fd.dec,fd.jan,fd.feb,fd.mar]
            months=['apr','may','jun','jul','aug','sep','oct','nov','dec','jan','feb','mar']
            monthtodisplay=['April','May','June','July','August','September','October','November','December','January','February','March']
            
            html=''
            counter=1
            for i in range(12):
                if feebymonth[i]!=None:
                    txn=ses.query(txns).filter_by(txnid=feebymonth[i]).first()
                    if txn:
                        h=f'<tr><th scope="row">{counter}</th><td>{monthtodisplay[i]}</td><td>{txn.amt}</td><td >{txn.date}</td><td >{feebymonth[i]}</td></tr>'
                        html=html+h
                        counter+=1

            return(render_template('dashboard_profile.html',name=pd.fname+' '+pd.lname,fname=fname,lname=lname,email=email,fathername=fathername,
                                        mothername=mothername,address=address,studentphone=studentphone,parentphone=parentphone,
                                        bloodgroup=bloodgroup,gender=gender,conveyance=conveyance,dob=dob,admno=admno,
                                        clas=clas,section=section,DOA=DOA,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,html=html))
        else:
            return(redirect('/login'))
    else:
        return(redirect('/login'))



@app.route('/dashboard/assignments')
def dash_assign():
     
     if 'logging_status' in session:
        if session['logging_status']==True:
            admno=session['admno']
            pd=ses.query(user_personal).filter_by(admno=(session['admno'])).first()
            fullname=pd.fname+' '+pd.lname
            return(render_template('dashboard_assignments.html',name=fullname))
        else:
            return(redirect('/login'))
     else:
         return(redirect('/login'))



@app.route('/dashboard/results')
def dash_result():
    if 'logging_status' in session:
        if session['logging_status']==True:
            admno=session['admno']
            pd=ses.query(user_personal).filter_by(admno=(session['admno'])).first()
            fullname=pd.fname+' '+pd.lname
            return(render_template('dashboard_results.html',name=fullname))
        else:
            return(redirect('/login'))
    else:
         return(redirect('/login'))


@app.route('/logout')
def logout():
    if 'logging_status' in session:
        if session['logging_status']==True:
            session['logging_status']=False
            session['admno']=None
            return(redirect('/login'))
        else:
            return(redirect('/login'))
    else:
         return(redirect('/login'))










@app.route('/adminlogout')
def adminlogout():
    if 'logging_status' in session:
        if session['admin_login_status']==True:
            session['admin_login_status']=False
            
            return(redirect('/admin'))
        else:
            return(redirect('/admin'))
    else:
         return(redirect('/admin'))



@app.route('/admin',methods=["GET","POST"])
def admin():
    if request.method=="GET":
        return(render_template('admin_login.html',alert_text=""))
    else:
        username=request.form['username'].strip()
        password=request.form['passwd'].strip()
        if username=="root" and password=='root':
            session['admin_login_status']=True
            return(redirect('/admin/dashboard'))
        else:
           return(render_template('admin_login.html',alert_text="Credentials didn't match!")) 


@app.route('/admin/dashboard')
def admin_dash():
    if "admin_login_status" in session  :
        if session['admin_login_status']==True:
            return(render_template('admin_base.html'))
        else:
            return(redirect('/admin'))

    else:
        return(redirect('/admin'))




@app.route('/admin/dashboard/addstudent',methods=["GET","POST"])
def admin_dash_addstudent():
    if request.method=="GET":
        ses.rollback()
        admno=(ses.query(user_personal).order_by(user_personal.admno.desc()).first().admno)+1

        return(render_template('admin_addstudent.html',admno=admno))
    else:
        ses.rollback()
        fname=request.form['fname']
        lname=request.form['laname']
        email=request.form['email']
        fathername=request.form['fathername']
        mothername=request.form['mothername']
        address=request.form['address']
        studentphone=request.form['studentphone']
        parentphone=request.form['parentphone']
        bloodgroup=request.form['bloodgroup']
        gender=request.form['gender']
        conveyance=request.form['conveyance']
        dob=request.form['dob']
        clas=request.form['class']
        section=request.form['section']
        admno=(ses.query(user_personal).order_by(user_personal.admno.desc()).first().admno)+1
        DOA=request.form['DOA']
        sub1=request.form['sub1']
        sub2=request.form['sub2']
        sub3=request.form['sub3']
        sub4=request.form['sub4']
        sub5=request.form['sub5']
        sub6=request.form['sub6']
        passwd=((fname[0:4])+(str(admno)[-4:])).upper()
        

        obj_user_personal=user_personal(fname=fname,lname=lname,email=email,fathername=fathername,
                                        mothername=mothername,address=address,studentphone=studentphone,parentphone=parentphone,
                                        bloodgroup=bloodgroup,gender=gender,conveyance=conveyance,dob=dob,passwd=passwd)
        obj_user_academic=user_academic(clas=clas,section=section,DOA=DOA,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6)
        obj_user_fees=user_fees(apr='',may='',jun='',jul= '',aug='',sep='',oct='',dec='',jan='',feb='',mar='' )
        ses.add(obj_user_academic)
        ses.add(obj_user_personal)
        ses.add(obj_user_fees)
        ses.commit()
        
        return(redirect('/admin/dashboard/addstudent'))





@app.route('/admin/dashboard/addfeedetail',methods=['POST',"GET"])
def admin_dash_addfeedetail():
    if request.method=="GET":
        rctnum=(ses.query(txns).order_by(txns.txnid.desc()).first().txnid)+1
        return(render_template('admin_addfeedetail.html',rctnum=rctnum))
    elif request.method=="POST":
        ses.rollback()
        admno=request.form['admno']
        month=request.form['month']
        paymentmethod=request.form['paymentmethod']
        paymentid=request.form['paymentid']
        amt=request.form['amt']
        rctnum=(ses.query(txns).order_by(txns.txnid.desc()).first().txnid)+1
        todaysdate=str(date.today().day)+'/'+str(date.today().month)+'/'+str(date.today().year)
        txn=txns(amt=amt,method=paymentmethod,date=todaysdate,paymentid=paymentid)
        fee=ses.query(user_fees).filter_by(admno=admno).one_or_none()
        # fee.oct="2300000099"
        print(type(fee.dec),fee.dec)
        x=f'fee.{month}="{rctnum}"'
        print(x)
        exec(x)
        ses.add(txn)
        ses.commit()
        print(admno,month,paymentmethod,amt)
        
        return(redirect('/admin/dashboard/addfeedetail'))
        
    else:
        return "METHOD ERROR"






@app.route('/savepdf')
def savepdf():
    return None
    





@app.route('/api/basicstudentdetail/<admno>')
def api_basicstudentdetails(admno):
    print(admno)
    pd=ses.query(user_personal).filter_by(admno=admno).first()
    ad=ses.query(user_academic).filter_by(admno=admno).first()
    fd=ses.query(user_fees).filter_by(admno=admno).first()
    feebymonth=[fd.apr,fd.may,fd.jun,fd.jul,fd.aug,fd.sep,fd.oct,fd.nov,fd.dec,fd.jan,fd.feb,fd.mar]
    months=['apr','may','jun','jul','aug','sep','oct','nov','dec','jan','feb','mar']
    monthtodisplay=['April','May','June','July','August','September','October','November','December','January','February','March']
    data={ 'name':(pd.fname+" "+pd.lname) , 'fathername':pd.fathername, 'clas':ad.clas+'-'+ad.section }
    html=''
    counter=1
    for i in range(12):
        if feebymonth[i]!=None:
            txn=ses.query(txns).filter_by(txnid=feebymonth[i]).first()
            if txn:
                print(dir(txn))
                h=f'<tr><th scope="row">{counter}</th><td>{monthtodisplay[i]}</td><td>{txn.amt}</td><td >{txn.date}</td><td >{feebymonth[i]}</td></tr>'
                html=html+h
                counter+=1
    print(feebymonth)
    data['html']=html
    return jsonify(data) , 200



@app.route('/api/experimental/<arg1>')
def api_experimental(arg1):
    args=arg1.split('+')
    a=args[0]
    b=args[1]
    return(f"<p> 1st:  {a} </p><p> 2nd:  {b} </p>")




if __name__=="__main__":
    

    app.run(debug=True)

