document.addEventListener('DOMContentLoaded', function() {
    $('td:contains("Miscellaneous")').closest('tr').css('background-color','lightsalmon');
    $('td:contains("Mortgage")').closest('tr').css('background-color','hotpink');
    $('td:contains("Rent")').closest('tr').css('background-color','orangered');
    $('td:contains("Entertainment")').closest('tr').css('background-color','darkkhaki');
    $('td:contains("Utilities")').closest('tr').css('background-color','mediumpurple');
    $('td:contains("Insurance")').closest('tr').css('background-color','mediumaquamarine');
    $('td:contains("Credit Cards")').closest('tr').css('background-color','steelblue');
    $('td:contains("Loans")').closest('tr').css('background-color','gainsboro');
});