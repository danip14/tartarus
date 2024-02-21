var tbTournament;
var modal_title;
var sede = localStorage.getItem('sede');

function detailsTeams(d) {
  let html = '';
  $.each(d.det, function (key, value) {
    html += `<hr><span> ${value.team.name}</span>`;
  });

  document.getElementById('detailsTeams').innerHTML = html;
  $('#modalDetails').show();
}


function getData() {
  tbTournament = $('#data').DataTable({
    ordering: true,
    searching: true,
    paging: true,
    info: false,
    pagingType: 'simple_numbers',
    responsive: true,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      data: {
        sede: sede,
        action: 'searchdata',
      },
      dataSrc: '',
    },
    dom: '<"myCustomClass"f>rt<"bottom"lp><"clear">',
    fnDrawCallback: function () {
      $("input[type='search']").attr('id', 'searchBox');
      $("input[type='search']").attr('autocomplete', 'off');
      $("select[name='data_length'], #searchBox").removeClass('input-sm');
      $('#searchBox').css('width', '350px').focus();
      $('#data').removeClass('dataTables_filter');
    },
    columns: [
      { data: 'name' },
      { data: 'datejoined' },
      { data: 'category.name' },
      { data: 'qtyLosses' },
      { data: 'status' },
      { data: 'id' },
    ],
    columnDefs: [
      {
        targets: [-3],
        class: 'text-center',
        orderable: false,
      },
      {
        targets: [-2],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          let status = '<span class="badge badge-primary">Creado</span>'
          if(data == 1){
            status = '<span class="badge badge-primary">Participantes Registrados</span>'
          }else if(data == 2){
            status = '<span class="badge badge-warning">Jugando</span>'
          }else if(data == 3){
            status = '<span class="badge badge-success">Finalizado</span>'
          } 
          return status
        }
      },
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          let buttons =
            '<a href="#" rel="edit" data-title="Editar" class="btn btn-warning btn-smp btn-flat"><i class="fas text-dark fa-edit"></i></a> ';
          if (row.status == 0)
          {
            buttons +=
              '<a href="#" rel="addTeams" data-title="Configurar Participantes" class="btn btn-info btn-smp btn-flat"><i class="fas text-dark fa-users"></i></a> ';
          }else{
            buttons +=
            '<a href="#" rel="details" data-title="Ver Participantes" class="btn btn-info btn-smp btn-flat"><i class="fas text-dark fa-search"></i></a> ';
            buttons +=
            '<a href="#" rel="go" data-title="Gestionar" class="btn btn-success btn-smp btn-flat"><i class="fas text-dark fa-sign"></i></a> ';
          }
          // buttons +=
          //   '<a href="#" rel="delete" data-title="Eliminar" type="button" class="btn btn-danger btn-smp btn-flat"><i class="fas text-dark fa-trash-alt"></i></a>';
          return buttons;
        },
      },
    ],
    initComplete: function (settings, json) {},
  });
}

$(function () {
  modal_title = $('.modal-title');
  $('#i_card_title').removeClass().addClass('text-dark fas fa-user-users');

  getData();

  $('#datejoined').datetimepicker({
    format: 'YYYY-MM-DD',
    date: moment().format('YYYY-MM-DD'),
    locale: 'es',
  });

  $('.btnAdd').on('click', function () {
    $('input[name="sede"]').val(sede);
    $('input[name="action"]').val('add');
    modal_title.find('span').html('Nuevo Torneo');
    document.getElementById('btn_submit').innerHTML =
      '<i class="fas fa-save"></i> Guardar';
    modal_title
      .find('#i_modal_title')
      .removeClass()
      .addClass('fas text-primary fa-plus');
    $('form')[0].reset();
    $('#modalTournament').modal('show');
  });

  $('#data tbody')
    .on('click', 'a[rel="details"]', function () {
      let tr = tbTournament.cell($(this).closest('td, li')).index();
      let data = tbTournament.row(tr.row).data();
      detailsTeams(data);
      $('#modalDetails').modal('show');
    })
    .on('click', 'a[rel="go"]', function () {
      let tr = tbTournament.cell($(this).closest('td, li')).index();
      let data = tbTournament.row(tr.row).data();
      window.open(`/panel/torneos/list/${data.id}/${data.lastRound}/`);
    })
    .on('click', 'a[rel="addTeams"]', function () {
      modal_title.find('span').html('Configurar Participantes del Torneo');
      modal_title
        .find('#i_modal_title')
        .removeClass()
        .addClass('fas text-primary fa-edit');
      document.getElementById('btn_submit').innerHTML =
        '<i class="fas fa-sync"></i> Registrar';
      let tr = tbTournament.cell($(this).closest('td, li')).index();
      let data = tbTournament.row(tr.row).data();
      $('input[name="tournamentId"]').val(data.id);
      getTeamsByCategory(data.category.id);
      $('#modalTeams').modal('show');
    })
    .on('click', 'a[rel="edit"]', function () {
      modal_title.find('span').html('Editar datos del torneo');
      modal_title
        .find('#i_modal_title')
        .removeClass()
        .addClass('fas text-primary fa-edit');
      document.getElementById('btn_submit').innerHTML =
        '<i class="fas fa-sync"></i> Actualizar';
      let tr = tbTournament.cell($(this).closest('td, li')).index();
      let data = tbTournament.row(tr.row).data();
      $('input[name="action"]').val('edit');
      $('input[name="id"]').val(data.id);
      $('input[name="name"]').val(data.name);
      $('select[name="category"]').val(data.category.id);
      $('input[name="datejoined"]').val(data.datejoined);
      $('input[name="qtyLosses"]').val(data.qtyLosses);
      $('#modalTournament').modal('show');
    })
    .on('click', 'a[rel="delete"]', function () {
      let tr = tbTournament.cell($(this).closest('td, li')).index();
      let data = tbTournament.row(tr.row).data();
      let parameters = new FormData();
      parameters.append('sede', sede);
      parameters.append('action', 'delete');
      parameters.append('id', data.id);
      submit_with_ajax_msj(
        window.location.pathname,
        'Notificación',
        '¿Está seguro de eliminar este registro?',
        parameters,
        function () {
          alertSweetSuccess('Listado de torneos actualizado');
          setTimeout(tbTournament.ajax.reload(), 5000);
        }
      );
    });

  $('.formTournament').on('submit', function (e) {
    e.preventDefault();
    convertToUpperCase();
    let parameters = new FormData(this);
    submit_with_ajax(window.location.pathname, parameters, function () {
      $('#modalTournament').modal('hide');
      alertSweetSuccess('Listado de torneos actualizado');
      location.reload();
    });
  });

  $('.formTeams').on('submit', function (e) {
    e.preventDefault();
    convertToUpperCase();
    let teams = getTeamsSelected();
    if(teams.length == 2){
      message_error('No ha seleccionado ningún participante')
      return
    }
    let parameters = new FormData(this);
    parameters.append('teams', teams)
    submit_with_ajax(window.location.pathname, parameters, function () {
      $('#modalTeams').modal('hide');
      alertSweetSuccess('Participantes Registrados');
      location.reload();
    });
  });
});


function getTeamsByCategory(category) {
  tbTeams = $('#dataTeams').DataTable({
    ordering: false,
    searching: false,
    paging: false,
    info: false,
    pagingType: 'simple_numbers',
    responsive: false,
    autoWidth: false,
    destroy: true,
    deferRender: true,
    ajax: {
      url: window.location.pathname,
      type: 'POST',
      data: {
        sede: sede,
        action: 'getTeams',
        category: category,
      },
      dataSrc: '',
    },
    dom: '<"myCustomClass"f>rt<"bottom"lp><"clear">',
    fnDrawCallback: function () {
      $('#data').removeClass('dataTables_filter');
    },
    columns: [
      { data: 'id' },
      { data: 'number' },
      { data: 'name' },
      { data: 'id' },
    ],
    columnDefs: [
      {
        targets: [-4],
        class: 'd-none',
        orderable: false,
      },
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          let checkbox ='<input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">';
          return checkbox;
        },
      },
    ],
    initComplete: function (settings, json) {},
  });
}


function getTeamsSelected(){
  seleccion = [];
  $(".tableTeams tr td input[type='checkbox']:checked").each(function(){
     row = $(this).closest('tr');
     seleccion.push(parseInt(row.find('td:eq(0)').text()));
  });

  seleccion = JSON.stringify(seleccion)
  return seleccion;
}