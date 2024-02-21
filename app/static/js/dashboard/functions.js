function get_graph_sales() {
  $.ajax({
    url: window.location.pathname,
    type: 'POST',
    data: {
      action: 'get_graph_sales',
    },
    dataType: 'json',
  })
    .done(function (data) {
      if (!data.hasOwnProperty('error')) {
        graphcolumn.addSeries(data);
        return false;
      }
      message_error(data.error);
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      alert(textStatus + ': ' + errorThrown);
    })
    .always(function (data) {
      console.log(data);
    });
}


$(function () {
  get_graph_sales();
});