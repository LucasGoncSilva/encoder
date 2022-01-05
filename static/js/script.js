window.addEventListener('DOMContentLoaded', () => {

    function checkASCII(str) { return /^[\x00-\x7F]*$/.test(str) }


    const message = document.getElementById('message')
    const keyword = document.getElementById('keyword')
    const confirm = document.querySelector('input[type=submit]')
    const output = document.getElementById('output')


    confirm.disabled = true
    confirm.style.cursor = 'not-allowed'


    document.querySelectorAll('.entry').forEach(() => {

        this.onkeyup = () => {

            if (message.value.length !== 0 && keyword.value.length !== 0) {

                confirm.disabled = false
                confirm.style.cursor = 'pointer'

            } else {

                confirm.disabled = true
                confirm.style.cursor = 'not-allowed'

            }
        }

    })



    document.querySelector('form').onsubmit = () => {

        if (checkASCII(message.value) === false || checkASCII(keyword.value) === false) {

            Swal.fire({
                icon: 'error',
                title: 'Deu ruim :(',
                html: '<p><span>NÃO</span> utilize caracteres especiais... Favor ler a legenda.</p>' +
                    '<p>Agradecido ;)</p>',
            })

            return false

        }

    }



    output.onclick = (e) => {

        if (output.value.length === 0) { return }

        let text = document.getElementById("output")

        text.select()
        text.setSelectionRange(0, 99999)

        navigator.clipboard.writeText(text.value)

        Swal.fire({
            title: 'Copiado!',
            icon: 'success',
            iconColor: '#4717f6',
            width: '300',
            showConfirmButton: false,
            timer: 1500
        })

    }

})