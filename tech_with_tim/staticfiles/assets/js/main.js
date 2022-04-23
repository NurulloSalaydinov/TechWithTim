// 'use strict';
(function () {
  document.querySelector('.nav-links').querySelectorAll('li').forEach(item => {
    item.onmouseenter = function (event) {
      move.css({
        opacity: 1,
        left: this.offsetLeft + 'px',
        width: this.offsetWidth + 'px'
      })
    }
    item.onmouseleave = function (event) {
      move.css({
        opacity: 0,
      })
    }
  })
})();
function checkSize() {
  if (window.innerWidth < 1124) {
    $('header .nav-links').slideUp(100);
  } else {
    $('header .nav-links').slideDown(100);
  }
  if (window.innerWidth < 768) {
    $('.share .hidden').addClass('open')
  } else {
    $('.share .icon:first-child').on('mouseenter', function (e) {
      $(this)[0].parentElement.querySelector('.hidden').classList.add('open')
    })
    $('.share').on('mouseleave', function (e) {
      $('.share .hidden').removeClass('open')
    })
  }
}
checkSize()
$(window).on('resize', checkSize)
$(function () {
  $(document).ready(function () {
    $('#teachers ._hidden').slideUp(1)
    $('#teachers .card .name span.fas').click(function () {
      $(this).parent().parent().children().eq(1).slideToggle(200)
      $(this).toggleClass('rotate')
    })
    $('#faq .hidden').slideUp();
    $('#faq .collapse[button]').click(function (e) {
      $(this).parent().parent().children().eq(1).slideToggle(200);
      $(this).parent().parent().toggleClass('active');
    })
    $('#faq li:not(.active) .question').click(function (e) {
      $(this).parent().parent().children().eq(1).slideToggle(200);
      $(this).parent().parent().toggleClass('active');
    })
  })
  $('.burger').click(e => {
    $('header .nav-links').slideToggle();
  })
  $('#hideform').click(e => {
    $('#contact #col').toggle(1000);
    document.querySelectorAll('#contact .absolute.img')[1].classList.toggle('_')

  })
  $("#openmodal").click(e => {
    $('.modal-container').show();
    $('.modal-container .modal').show(1000);
  })
  $('.modal-container').hide();
  $("#closemodal").click(e => {
    $('.modal-container .modal').hide(1000);
    setTimeout(() => {
      $('.modal-container').hide();
    }, 900)
  })
})

var splide = new Splide('#splide4', {
  type: 'loop',
  padding: '5rem',
  perPage: 2,
  focus: 'center',
  gap: '20px',
  autoplay: true,
  perMove: 1,
  breakpoints: {
    767: {
      perPage: 1,
      padding: 0,
      gap: 0,
      autoWidth: false
    },
    1950: {
      perPage: 4
    },
    1500: {
      perPage: 2
    },

  }
});
splide.mount()


var splide2 = new Splide('#splide3', {
  // type   : 'loop',
  padding: '5rem',
  gap: '15px',
  perMove: 1,
  // autoWidth: true,
  perPage: 1,
  arrows: false,
  // focus: 'center',
  autoplay: true,
  breakpoints: {
    767: {
      perPage: 1,
      padding: 0,
      gap: 0,
      autoWidth: false
    },
    1950: {
      perPage: 3
    },
    1500: {
      perPage: 2
    },

  }
});
splide2.mount()

var splide3 = new Splide('#splide2', {
  // type   : 'loop',
  perMove: 1,
  padding: '5rem',
  gap: '15px',
  autoWidth: true,
  perPage: 1,
  arrows: false,
  // focus: 'center',
  autoplay: true,
  breakpoints: {
    767: {
      perPage: 1,
      padding: 0,
      autoWidth: false
    },
    1950: {
      perPage: 4,
      focus: 'center'
    },
    1500: {
      perPage: 1
    },

  }
});
splide3.mount()

var splide1 = new Splide('#splide1', {
  // type   : 'loop',
  perMove: 1,
  padding: '5rem',
  gap: '15px',
  perPage: 1,
  autoWidth: true,
  arrows: false,
  // focus: 'center',
  autoplay: true,
  breakpoints: {
    767: {
      perPage: 1,
      gap: 0,
      padding: 0,
      autoWidth: false
    },
    1950: {
      perPage: 4,
      autoWidth: true
    },
    1500: {
      perPage: 1,
      autoWidth: true
    },

  }
});
splide1.mount()
