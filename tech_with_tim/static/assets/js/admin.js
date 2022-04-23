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
    $('.modal .box').css('display', 'none');
    console.log(modal)
    if (modal.self && modal.opener && modal.closer) {
        modal.opener.addEventListener('click', function () {
            $('.modal').css('display', 'flex');
            $('.modal .box').css('display', 'block');
        })
        modal.closer.addEventListener('click', function () {
            $('.modal .box').css('display', 'none');
            $('.modal').css('display', 'none')  ;
        })
    }
})();