

let modal =document.getElementById('myModel');


function display1(){
    modal.style.display = "block";
    let studsession = document.getElementById('session').value;
    let studName = document.getElementById('name1').value;
    let studFName = document.getElementById('name2').value;
    let studadmission = document.getElementById('categoryno').value;
    let studdescription = document.getElementById('description').value;
    let studbatch = document.getElementById('batch').value;
    let studdiscipline = document.getElementById('discipline').value;
    let studrollno = document.getElementById('rollno').value;
    let studseatno = document.getElementById('seatno').value;
    let studsign = document.getElementById('applicantsign').value;
    let studfathername = document.getElementById('fathername').value;
    let studapplicant = document.getElementById('Applicantname').value;
    let studguardian1 = document.getElementById('applicant1name').value;
    let studfathersign = document.getElementById('fathersign').value;
    let studnewdept = document.getElementById('newdept').value;
    let studnewrollno = document.getElementById('newroll').value;
    let deanSign = document.getElementById('deansign').value;
    let registrarSign = document.getElementById('registrarsign').value;
    


    console.log(studName);
    document.getElementById('session1').innerHTML = studsession;
    document.getElementById('studName').innerHTML = studName;
    document.getElementById('studFatherName').innerHTML = studFName;
    document.getElementById('studadmission').innerHTML = studadmission;
    document.getElementById('studdescription').innerHTML = studdescription;
    document.getElementById('studbatch').innerHTML = studbatch;
    document.getElementById('studdiscipline').innerHTML = studdiscipline;
    document.getElementById('studrollno').innerHTML = studrollno;
    document.getElementById('studseatno').innerHTML = studseatno;
    document.getElementById('studsign').innerHTML = studsign;
    document.getElementById('studGuardianName').innerHTML = studfathername;
    document.getElementById('studApplicantName').innerHTML = studapplicant;
    document.getElementById('studGuardian1Name').innerHTML = studguardian1;
    document.getElementById('studGuardiansign').innerHTML = studfathersign;
    document.getElementById('studnewdept').innerHTML = studnewdept;
    document.getElementById('studnewrollno').innerHTML = studnewrollno;
    document.getElementById('dean1sign').innerHTML = deanSign;
    document.getElementById('registrar1sign').innerHTML = registrarSign;
    

    

}

function closeModal(){
    modal.style.display = "none";
}