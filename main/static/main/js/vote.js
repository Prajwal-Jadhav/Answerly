const upvote_button = document.getElementById('up')

data = JSON.stringify({})

function send_voting_request(event) {
  fetch(`http://localhost:8000/questions/${question_id}/vote/${this.getAttribute('id')}`, {
    method: 'POST',
    headers: {
      "X-CSRFToken": csrftoken
    }
  })
  .then(response => console.log(response.json()))
  .catch(error => console.log(error))
}

upvote_button.addEventListener("click", send_voting_request, false)