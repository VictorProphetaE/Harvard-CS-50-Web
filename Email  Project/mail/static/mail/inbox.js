document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').onsubmit = email_send;

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch(`/emails/${mailbox}`)
  .then((response) => response.json())
  .then((emails) => {
    emails.forEach(email => {
      const email_header = document.createElement("div");
      acti = email.read ? "Inactive" : "Active";
      email_header.innerHTML= `
      <table class='table'>
          <tbody>
            <tr class =`+ acti +` id="tab">
              <td><span>${email.sender}</span></td>
              <td><span> ${email.subject} </span></td>
              <td><span> ${email.timestamp} </span></td>
            </tr>
          </tbody>
      </table>`;     

      email_header.addEventListener('click', () => open_mail(email.id,mailbox));
      document.querySelector('#emails-view').appendChild(email_header);
    });

    var tables = Array.from (document.querySelectorAll("#tab"))
    tables.forEach((email, index) => {
        if("sent" === mailbox || "archive" === mailbox){
          console.log(tables[index]);
          tables[index].className  += "White";
      }
    });
  })
}

function email_send(){

  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;
  
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body,
    }),
  })
    .then((response) => response.json())
    .then((result) => {
      alert("Your email has been sent");
      load_mailbox('sent',result);
      console.log(result);
    })
    .catch((error) => console.log(error));
    return false;
}

function open_mail(mail_id,mailbox){

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  fetch(`/emails/${mail_id}`)
  .then(response => response.json())
  .then(email => {
    const read_mail = document.querySelector('#email-view');
    archi = email.archived ? "Unarchive" : "Archive";
    button = email.archived ? "Unarchive" : "Archive";
    read_mail.innerHTML =`
    <table class="table table-borderless" id = "readmail">
        <tr>
          <td><strong>From: </strong>${email.sender} </td>
        </tr>
        <tr>
          <td><strong>To: </strong>${email.recipients}</td>
        </tr>
        <tr>
          <td><strong>Subject: </strong> ${email.subject}</td>
        </tr>
        <tr>
          <td><strong>Timestamp: </strong>${email.timestamp} </td>
        </tr>
        <td><button class="button1" id="reply" onclick="reply('${email.id}');">Reply</button></td>
        <td><div class="button-loc" id="archiveme" ><button class=`+button+` onclick="archiveemail(${email.id}, ${email.archived});">`+archi+`</button></div></td>
    </table>
    <p>${email.body}</p>
    `;

    if(email.recipients !== email.sender && "sent" === mailbox){
      document.querySelector('#archiveme').remove()
      document.querySelector('#reply').remove()
    }

    fetch(`/emails/${email.id}`, {
      method: 'PUT',
      body: JSON.stringify({
          read: true
      })
  }).then();

  })
  .catch((error) => console.log(error));
}

function archiveemail(emailid, archive) {
  fetch(`/emails/${emailid}`, {
      method: 'PUT',
      body: JSON.stringify({
          archived: !archive
      })
  }).then(() => {
    load_mailbox("inbox");
  })
  .catch(error =>console.log(error));
  
}

function reply(emailid){

  fetch(`/emails/${emailid}`)
  .then(response => response.json())
  .then(email => {    
    const rep =  email.subject.slice(0,2) === "Re: " ? email.subject : "Re: " + email.subject ;
    const bod = `On ${email.timestamp} ${email.sender} wrote: ${email.body} `;
    const sen = ` ${email.sender}`;

    //document.querySelector('#compose-recipients').setAttribute('disabled', '');
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#email-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';

    document.querySelector('#compose-recipients').value = sen;
    document.querySelector('#compose-subject').value = rep;
    document.querySelector('#compose-body').value = bod;

  })
  .catch(error =>console.log(error));

}