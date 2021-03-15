
function send_question_voting_request(action, question_id, vote_count_element) {

  fetch(`${window.location.origin}/questions/${question_id}/vote/${action}`, {
    method: 'POST',
    headers: {
      "X-CSRFToken": csrftoken
    }
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        vote_count_element.innerHTML = data.total_votes;
      } else {
        throw { "error": true };
      }
    })
    .catch(error => console.log(error));
}


function handleQuestionVote(clicked_button, question_id) {
  let all_siblings = Array.from(clicked_button.parentNode.childNodes).filter(elem => elem.localName === 'div');
  let upvote_answer_button = all_siblings[0];
  let downvote_answer_button = all_siblings[2];
  let question_vote_count = all_siblings[1];

  let action = clicked_button.dataset.action;

  if (action === 'delete') {
    clicked_button.classList.remove('user_voted');

    if (clicked_button === upvote_answer_button) { clicked_button.dataset.action = 'up'; }
    else if (clicked_button === downvote_answer_button) { clicked_button.dataset.action = 'down'; }
  }
  else if (clicked_button === upvote_answer_button) {
    clicked_button.classList.add('user_voted');
    clicked_button.dataset.action = 'delete';
    downvote_answer_button.classList.remove('user_voted');
    downvote_answer_button.dataset.action = 'down';
  }
  else if (clicked_button === downvote_answer_button) {
    clicked_button.classList.add('user_voted');
    clicked_button.dataset.action = 'delete';
    upvote_answer_button.classList.remove('user_voted');
    upvote_answer_button.dataset.action = 'up';
  }

  send_question_voting_request(action, question_id, question_vote_count);
}