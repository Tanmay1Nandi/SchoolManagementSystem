
admnoinput=document.getElementById('admnoinput');
nameplaceholder=document.getElementById('name');
fathernameplaceholder=document.getElementById('fathername');
classplaceholder=document.getElementById('clas');
paymentmethod=document.getElementById('paymentmethod')
paymentidlbl=document.getElementById('paymentidlbl')
paymentid=document.getElementById('paymentid')
let months=['apr','may','jun','jul','aug','sep','oct','nov','dec','jan','feb','mar']
table=document.getElementById('table')





async function search()  {
    admno=admnoinput.value;
    if (admno.trim()==''){
        alert("Can not be empty!!")
    }
    else{
        let promise= await fetch('/api/basicstudentdetail/'+admno);
        console.log(promise.status)
        if (promise.status==200){
            let response= await promise.json();
            

            console.dir(response);
            
            nameplaceholder.placeholder=response['name'];
            fathernameplaceholder.placeholder=response['fathername']
            classplaceholder.placeholder=response['clas']
            table.innerHTML=response['html']    

        }
        else{
            alert("Invalid Admission Number")
        }
    }   
}





function select(){
    val=paymentmethod.value;
    if (val=="cash"){
        paymentidlbl.innerHTML="<p style=' padding: 0;margin:0; visibility: hidden;'>a</p>";
        paymentid.readOnly=true;
        paymentid.value=''
        paymentid.style.visibility="hidden";
    }
    else if (val=="cheque"){
        paymentidlbl.innerHTML='Cheque Number:';
        paymentid.readOnly=false;
        paymentid.value='';
        paymentid.style.visibility="visible";
    
    }
    else if (val=="UPI"){
        paymentidlbl.innerHTML='UPI ID/ Number:'  ;
        paymentid.readOnly=false;
        paymentid.value='';
        paymentid.style.visibility="visible";
    }
    console.log(paymentmethod.value);
}
