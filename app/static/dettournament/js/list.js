var tableDetTournament;
var tbDetTournament;
var sede = localStorage.getItem('sede');
var sede_id = 0;

$(function () {
  $('.selectViewRound').on('change', function() {
    let tournament = $('input[name="idtornaument"]').val()
    let round = this.value;

    window.open(`/panel/torneos/list/${tournament}/${round}/`, "_self");
  });

});

$(function () {
  $('#confrontations').on('submit', function (e) {
    e.preventDefault();
    let teams = getdataDict();
    let parameters = new FormData();
    parameters.append('action', 'RecordResults')
    parameters.append('teams', teams)
    submit_with_ajax(window.location.pathname, parameters, function () {
      alertSweetSuccess('Resultados Registrados');
      setTimeout(location.reload(), 5000);
    });
  });

});

function getdataDict(){
  let array = []
  let form = document.forms.namedItem("confrontations");
  let parameters = new FormData(form);

  let count = 0
  let temp = []
  parameters.forEach(function(value, key){
    if(count == 4){
      array.push(temp)
      count = 0
      temp = []
    }

    temp.push(parseInt(value))
    count += 1
  });

  array.push(temp)
  array = JSON.stringify(array)

  return array;
}


function checkWin(qty1, qty2, class1, class2){
  let value1 = parseInt($(`input[name=${qty1}]`).val());
  let value2 = parseInt($(`input[name=${qty2}]`).val());

  let element1 = document.getElementById(class1);
  let element2 = document.getElementById(class2);

  console.log(value1, value2)

  if (value1 > value2){
    element1.classList.remove("bg-secondary");
    element1.classList.add("bg-success");

    element2.classList.remove("bg-success");
    element2.classList.add("bg-secondary");
  } else if(value1 == value2){

    element1.classList.remove("bg-secondary");
    element1.classList.remove("bg-success");
    element1.classList.add("bg-success");

    element2.classList.remove("bg-secondary");
    element2.classList.remove("bg-success");
    element2.classList.add("bg-success");

  } else{

    element1.classList.remove("bg-success");
    element1.classList.add("bg-secondary");

    element2.classList.remove("bg-secondary");
    element2.classList.add("bg-success");
  }
}

function generateRound(){
  let parameters = new FormData();
  parameters.append('action', 'GenerateNewRound')
  submit_with_ajax(window.location.pathname, parameters, function (response) {
    alertSweetSuccess('Nueva Ronda Generada');
    window.open(`/panel/torneos/list/${response.id}/${response.round}/`, "_self");
  });
}