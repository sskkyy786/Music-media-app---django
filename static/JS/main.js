
// let comment_icon = document.querySelectorAll('.c');
// // let post_id = document.querySelector('#' + pos.id);


// comment_icon.forEach(comment_ic => {
//     comment_ic.addEventListener('click', () => {
//         console.log('hi')
//         let comment_box = document.querySelectorAll('.comment-box');
//         if (comment_box.style.display === 'none') {
//             comment_box.style.display = 'block';
//           } else {
//             comment_box.style.display = 'none';
//           }
//     });
// });




// let comment_icons = document.querySelectorAll('.c');

// comment_icons.forEach(comment_icon => {
//     comment_icon.addEventListener('click', () => {
//         console.log('hi');
//         let comment_boxes = document.querySelectorAll('.comment-box');

//         comment_boxes.forEach(comment_box => {
//             if (comment_box.style.display === 'none' || comment_box.style.display === '') {
//                 comment_box.style.display = 'block';
//             } else {
//                 comment_box.style.display = 'none';
//             }
//         });
//     });
// });




let comment_icons = document.querySelectorAll('.c');

comment_icons.forEach(comment_icon => {
    comment_icon.addEventListener('click', () => {
        console.log('hi');
        let postId = comment_icon.dataset.postId;
        let comment_box = document.querySelector(`.comment-box[data-post-id="${postId}"]`);

        if (comment_box.style.display === 'none' || comment_box.style.display === '') {
            comment_box.style.display = 'block';
        } else {
            comment_box.style.display = 'none';
        }
    });
});


(function () {
    'use strict'
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl)
    })
  })()



















