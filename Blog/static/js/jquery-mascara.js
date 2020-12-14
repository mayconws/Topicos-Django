$(document).ready(function () {

    $("#id_cpf").mask("000.000.000-00", { placeholder: "000.000.000-00" });

    $('#id_data').mask("00/00/0000", { placeholder: "__/__/____" });

    $('#id_nome_categoria').attr("placeholder", "Digite o nome da categoria");

    $('#id_titulo').attr("placeholder", "Digite o nome do titulo");

    $('#id_conteudo').attr("placeholder", "Digite aqui...");

    $('#id_nome_comentario').attr("placeholder", "Digite o nome");

    $('#id_email').attr("placeholder", "usuario@usuario.com");

    $('#id_nome_perfil').attr("placeholder", "Digite o nome");

    $('#id_email_perfil').attr("placeholder", "usuario@usuario.com");

    $('#id_endereco').attr("placeholder", "Digite o endereço");

    var SPMaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
    },
        spOptions = {
            onKeyPress: function (val, e, field, options) {
                field.mask(SPMaskBehavior.apply({}, arguments), options);
            }
        };

    $('#id_telefone').mask(SPMaskBehavior, spOptions,);

});