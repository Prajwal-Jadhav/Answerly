
function handleAnswerVote(clicked_button, answer_id) {
  all_siblings = Array.from(clicked_button.parentNode.childNodes).filter(elem => elem.localName === 'div');
  upvote_answer_button = all_siblings[0];
  downvote_answer_button = all_siblings[2];
  answer_vote_count = all_siblings[1];

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
}