document.addEventListener('DOMContentLoaded', function() {
    let button = document.querySelectorAll(".btneditpat");
    let button1 = document.querySelectorAll(".btneditappointment");

    button.forEach((element) => {
      updateelement(element);
    });

    button1.forEach((element) => {
        updatepatielement(element);
      });

});

function updateelement(element){
    element.addEventListener("click", function(event) {
        event.preventDefault();
        $('#modaledit').on('show.bs.modal', () => {
            var saveButton = document.querySelector(".modal-footer > #savepatient");
            tr_id = null;
            name = null;
            email = null;
            address = null;
            phone = null;
            id = element.getAttribute("idpatient");

            if (id) {
                
                tr_id = "#patient" + id;
                name1 = $(tr_id).find(`#userName${id}`).text();
                email1 = $(tr_id).find(`#userEmail${id}`).text();
                address1 = $(tr_id).find(`#userAddress${id}`).text();
                phone1 = $(tr_id).find(`#userPhone${id}`).text();
                $('#form-name').val(name1);
                $('#form-email').val(email1);
                $('#form-address').val(address1);
                $('#form-phone').val(phone1);
            }
            saveButton.addEventListener("click", () => {
                var nameInput = $('input[name="formName"]').val().trim();
                var emailInput = $('input[name="formEmail"]').val().trim();
                var addressInput = $('input[name="formAddress"]').val().trim();
                var phoneInput = $('input[name="formPhone"]').val().trim();
                fetch('/updatepatient/'+ id, {
                    method: "POST",
                    body: JSON.stringify({
                        name: nameInput,
                        email: emailInput,
                        address: addressInput,
                        phone: phoneInput,
                    }),
                })
                .then(async(response) => {
                    if (response.status === 201) {
                        document.querySelector(`#userName${id}`).innerHTML = nameInput;
                        document.querySelector(`#userEmail${id}`).innerHTML = emailInput;
                        document.querySelector(`#userAddress${id}`).innerHTML = addressInput;
                        document.querySelector(`#userPhone${id}`).innerHTML = phoneInput;
                    }
                })
                return false;
            });
            event.stopPropagation();
        });
    });
}

function updatepatielement(element){
    element.addEventListener("click", function(event) {
        event.preventDefault();
        $('#modaledit1').on('show.bs.modal', () => {
            var saveButton = document.querySelector(".modal-footer > #saveappointment");
            tr_id1 = null;
            date = null;
            time = null;

            id = element.getAttribute("idappointment");

            if (id) {
                
                tr_id1 = "#appointment" + id;
                doc1 = $(tr_id1).find(`#DocName${id}`);
                date1 = $(tr_id1).find(`#AppoiDate${id}`);
                time1 = $(tr_id1).find(`#AppoiTime${id}`);
                $('#form-doc').val(doc1);
                $('#form-date').val(date1);
                $('#form-time').val(time1);
                
            }
            
            saveButton.addEventListener("click", () => {
                var dateInput = $('input[name="formDate"]').val();
                var timelInput = $('input[name="formTime"]').val();
                teste1 = $('#select_doctor option:selected').text()
                console.log(teste1)
                $('#modaledit1').modal('hide');
                fetch('/updateappointme/'+ id, {
                    method: "POST",
                    body: JSON.stringify({
                        doctor: teste1,
                        date: dateInput,
                        time: timelInput,
                    }),
                })
                .then(async(response) => {
                    if (response.status === 201) {
                        document.querySelector(`#DocName${id}`).innerHTML = teste1;
                        document.querySelector(`#AppoiDate${id}`).innerHTML = dateInput;
                        document.querySelector(`#AppoiTime${id}`).innerHTML = timelInput;
                    }
                })
                return false;
            });
            event.stopPropagation();
        });
    });
}
