document.addEventListener('DOMContentLoaded', function() {
    $('tr#category-row td:contains("Miscellaneous")').closest('tr').css('background-color','lightsalmon');
    $('tr#category-row td:contains("Mortgage")').closest('tr').css('background-color','hotpink');
    $('tr#category-row td:contains("Rent")').closest('tr').css('background-color','orangered');
    $('tr#category-row td:contains("Entertainment")').closest('tr').css('background-color','darkkhaki');
    $('tr#category-row td:contains("Utilities")').closest('tr').css('background-color','mediumpurple');
    $('tr#category-row td:contains("Insurance")').closest('tr').css('background-color','mediumaquamarine');
    $('tr#category-row td:contains("Credit Cards")').closest('tr').css('background-color','steelblue');
    $('tr#category-row td:contains("Loans")').closest('tr').css('background-color','gainsboro');

    $("td#category-color[data-category='Miscellaneous']").css('background-color','lightsalmon')
    $("td#category-color[data-category='Mortgage']").css('background-color','hotpink')
    $("td#category-color[data-category='Rent']").css('background-color','orangered')
    $("td#category-color[data-category='Entertainment']").css('background-color','darkkhaki')
    $("td#category-color[data-category='Utilities']").css('background-color','mediumpurple')
    $("td#category-color[data-category='Insurance']").css('background-color','mediumaquamarine')
    $("td#category-color[data-category='Credit Cards']").css('background-color','steelblue')
    $("td#category-color[data-category='Loans']").css('background-color','gainsboro')

    $("div#category-color[data-category='Miscellaneous']").css('background-color','lightsalmon')
    $("div#category-color[data-category='Mortgage']").css('background-color','hotpink')
    $("div#category-color[data-category='Rent']").css('background-color','orangered')
    $("div#category-color[data-category='Entertainment']").css('background-color','darkkhaki')
    $("div#category-color[data-category='Utilities']").css('background-color','mediumpurple')
    $("div#category-color[data-category='Insurance']").css('background-color','mediumaquamarine')
    $("div#category-color[data-category='Credit Cards']").css('background-color','steelblue')
    $("div#category-color[data-category='Loans']").css('background-color','gainsboro')
});