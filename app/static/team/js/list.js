var tbTeam;
var modal_title;
var sede = localStorage.getItem('sede');
var sede_id = 0;

function getData() {
  $('#i_card_title').removeClass().addClass('text-dark fas fa-boxes');
  $('#i_card_title2').removeClass().addClass('text-dark fas fa-th-list');

  tbTeam = $('#data').DataTable({
    ordering: true,
    searching: true,
    paging: true,
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
        action: 'searchdata',
      },
      dataSrc: '',
    },
    columns: [
      { data: 'name' },
      { data: 'dni' },
      { data: 'birthdate' },
      { data: 'gender' },
      { data: 'email' },
      { data: 'category.name' },
      { data: 'id' },
    ],
    dom: '<"myCustomClass"f>rt<"bottom"lp><"clear">',
    fnDrawCallback: function () {
      $("input[type='search']").attr('id', 'searchBox');
      $("input[type='search']").attr('autocomplete', 'off');
      $("select[name='data_length'], #searchBox").removeClass('input-sm');
      $('#searchBox').css('width', '350px').focus();
      $('#data').removeClass('dataTables_filter');
    },
    columnDefs: [
      {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
          let buttons =
            '<a href="#" rel="edit" data-title="Editar datos" type="button" class="btn btn-warning btn-smp btn-flat"><i class="fas text-dark fa-edit"></i></a> ';
          buttons +=
            '<a href="#" rel="delete" data-title="Eliminar" type="button" class="btn btn-danger btn-smp btn-flat"><i class="fas text-dark fa-trash-alt"></i></a> ';
          return buttons;
        },
      },
    ],
  });
}

$(function () {

  modal_title = $('.modal-title');
  getData();

  $('#datejoined').datetimepicker({
    format: 'YYYY-MM-DD',
    date: moment().format('YYYY-MM-DD'),
    maxDate : 'now',
    locale: 'es',
  });

  if ($('input[name="group"]').val() == 1) {
    tbTeam.column(-1).visible(false);
    tbTeam.column(-4).visible(false);
  }

  $('.btnAdd').on('click', function () {
    $('form')[0].reset();
    modal_title.find('#span_modal_title').html('Agregar Participante');
    modal_title
      .find('#i_modal_title')
      .removeClass()
      .addClass('fas text-primary fa-plus');
    document.getElementById('btn_submit').innerHTML =
      '<i class="fas fa-save"></i> Guardar';
    $('input[name="action"]').val('add');
    $('input[name="sede"]').val(sede);
    $('#modalTeam').modal('show');
  });

  $('.btnAddCategory').on('click', function () {
    $('form')[1].reset();
    $('input[name="sede"]').val(sede);
    $('input[name="action"]').val('addCategory');
    $('#modalCategory').modal('show');
  });

  $('#data tbody')
    .on('click', 'a[rel="edit"]', function () {
      $('form')[0].reset();
      modal_title.find('#span_modal_title').html('Editar datos del participante');
      modal_title
        .find('#i_modal_title')
        .removeClass()
        .addClass('fas text-primary fa-edit');
      document.getElementById('btn_submit').innerHTML =
        '<i class="fas fa-sync"></i> Actualizar';
      let tr = tbTeam.cell($(this).closest('td, li')).index();
      let data = tbTeam.row(tr.row).data();
      $('input[name="sede"]').val(sede);
      $('input[name="action"]').val('edit');
      $('input[name="id"]').val(data.id);
      $('input[name="name"]').val(data.name);
      $('input[name="dni"]').val(data.dni);
      $('input[name="birthdate"]').val(data.birthdate);
      $('select[name="gender"]').val(data.gender);
      $('input[name="email"]').val(data.email);
      $('select[name="category"]').val(data.category.id);
      $('#modalTeam').modal('show');
    })
    .on('click', 'a[rel="delete"]', function () {
      let tr = tbTeam.cell($(this).closest('td, li')).index();
      let data = tbTeam.row(tr.row).data();
      let parameters = new FormData();
      parameters.append('sede', sede);
      parameters.append('action', 'delete');
      parameters.append('id', data.id);
      submit_with_ajax_msj(
        window.location.pathname,
        'Notificación',
        '¿Estas seguro de realizar eliminar el siguiente registro?',
        parameters,
        function () {
          alertSweetSuccess('Listado de Equipos actualizado');
          setTimeout(tbTeam.ajax.reload(), 5000);
        }
      );
    });

  $('.formTeam').on('submit', function (e) {
    e.preventDefault();
    convertToUpperCase();
    let parameters = new FormData(this);
    submit_with_ajax(window.location.pathname, parameters, function () {
      $('#modalTeam').modal('hide');
      alertSweetSuccess('Listado de participantes actualizado');
      setTimeout(tbTeam.ajax.reload(), 5000);
    });
  });

  $('.formCategory').on('submit', function (e) {
    e.preventDefault();
    convertToUpperCase();
    let parameters = new FormData(this);
    submit_with_ajax(window.location.pathname, parameters, function () {
      $('#modalCategory').modal('hide');
      alertSweetSuccess('Nueva categoría registrada');
      setTimeout(window.location.reload(), 5000);
    });
  });

  $('.btnAddTournament').on('click', function () {
      let parameters = new FormData();
      parameters.append('sede', sede);
      parameters.append('action', 'registerTournament');
      submit_with_ajax(window.location.pathname, parameters, function () {
        alertSweetSuccess('Nuevo torneo registrado');
        setTimeout(window.location.reload(), 5000);
      });
  });

  $('.btnAddTournamentTeams').on('click', function () {
    let parameters = new FormData();
    parameters.append('sede', sede);
    parameters.append('action', 'registerTournamentTeams');
    submit_with_ajax(window.location.pathname, parameters, function () {
      alertSweetSuccess('Equipos registrados');
      setTimeout(window.location.reload(), 5000);
    });
  });
});
