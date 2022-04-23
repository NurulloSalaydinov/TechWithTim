// this function is for cards to set  their background color
var no_emojis = ['\(^Д^)/', '(^_^)b', '(^-^*)', '\(o_o)/', '(o^^)o', "(='X'=)", "(≥o≤)", "(;-;)", '(·_·)', '(>_<)', '(˚Δ˚)', '(·_· )', '( ·_·)']

    ; (function () {
        const colors = ['#62BFC4', '#9081D7', '#FD2A3F', '#2CB8DF', '#52D344']
        const colorElement = document.querySelectorAll('.mini-cards .cardy');
        if (colors.length == colorElement || colorElement.length > colors) {
            for (let i = 0; i < colorElement.length; i++) {
                colorElement[i].style.backgroundColor = colors[i];
            }
        } else {
            for (let i = 0; i < colorElement.length - colors.length; i++) {
                var generateColor = "#" + Math.floor(Math.random() * 0xFFFFFF).toString(16);
                colors.push(generateColor);
            }
            for (let i = 0; i < colorElement.length; i++) {
                colorElement[i].style.backgroundColor = colors[i];
            }
        }
        console.log(colorElement)
    })()

    ; (function () {
        var leftPanel = document.querySelector('.left-panel');
        leftPanel.classList.add('collapsed')
        document.querySelector('.toggler-icon').addEventListener('click', function () {
            leftPanel.classList.toggle('collapsed');
            document.querySelector('[main].container').classList.toggle('active');
            setTimeout(() => {
                leftPanel.querySelectorAll('a').forEach(e => e.style.display = 'none')
            }, 500)
        })
    })()
    ;
; (function () {
    const modal = {
        self: document.querySelector('.modal'),
        opener: document.querySelector('#open'),
        closer: document.querySelector('#hide')
    }
    $('.modal .box').hide(500);
    console.log(modal)
    if (modal.self && modal.opener && modal.closer) {
        modal.opener.addEventListener('click', function () {
            $('.modal').show();
            $('.modal .box').show(500);
        })
        modal.closer.addEventListener('click', function () {
            $('.modal .box').hide(500);
            setTimeout(() => {
                $('.modal').hide();
            }, 500)
        })
    }
})();


function _delete(el) {
    el = el.parentElement.parentElement.parentElement;

    function delete_from_django() {
        // your code here
        // var xhr = new XMLHttpRequest();
        // xhr.open('POST', '/admin/delete_sms/', true);
        // xhr.setRequestHeader('Content-Type', 'application/json');
        // xhr.send(JSON.stringify({
        //     id: el.id

        // }));
        // xhr.onload = function () {
        //     if (this.status == 200) {
        //         el.remove();
        //     }
        // }
    }

    function _add(_) {
        el.parentElement.parentElement.classList.add('empty');
        el.parentElement.parentElement.setAttribute('data-emoji', _)
    }
    var random_emoji = no_emojis[Math.floor(Math.random() * no_emojis.length)];
    isEmpty(0) ? _add(random_emoji) : null;
}

function isEmpty(n) {
    return document.querySelectorAll('.messages .sms').length <= n ? true : false;
}

if (isEmpty(0)) {
    var random_emoji = no_emojis[Math.floor(Math.random() * no_emojis.length)];
    try {
        document.querySelector('.messages').classList.add('empty');
        document.querySelector('.messages').setAttribute('data-emoji', random_emoji)
    } catch (err) {
        console.log('ERRRRROR', err, '\n', document.querySelector('.messages'), random_emoji)
    }
}