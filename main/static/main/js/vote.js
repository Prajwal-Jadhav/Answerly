const upvote_button = document.getElementById('up');
const downvote_button = document.getElementById('down');
const question_votes_count = document.querySelector(".question_votes__count");

data = JSON.stringify({});

function send_voting_request(event) {
  const clicked_button_id = this.getAttribute('id');
  let action = clicked_button_id;

  if (upvote_button.dataset.hasvoted === 'yes' || downvote_button.dataset.hasvoted === 'yes') {

    let previous_command;

    if (upvote_button.dataset.hasvoted === 'yes') {
      previous_command = 'up';
    } else {
      previous_command = 'down';
    }

    if (previous_command === action) {
      action = 'delete';
    }
  }

  if (action == 'delete') {
    this.classList.remove('user_voted');
    this.dataset.hasvoted = 'no';

  } else {
    this.classList.add('user_voted');
    this.dataset.hasvoted = 'yes';

    if (this == upvote_button) {

      downvote_button.dataset.hasvoted = 'no';
      downvote_button.classList.remove('user_voted');

    } else {
      upvote_button.dataset.hasvoted = 'no';
      upvote_button.classList.remove('user_voted');
    }
  }

  console.log(action);

  fetch(`http://localhost:8000/questions/${question_id}/vote/${action}`, {
    method: 'POST',
    headers: {
      "X-CSRFToken": csrftoken
    }
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        question_votes_count.innerHTML = data.total_votes;
      } else {
        throw { "error": true };
      }
    })
    .catch(error => console.log(error));
}

upvote_button.addEventListener("click", send_voting_request);
downvote_button.addEventListener("click", send_voting_request);