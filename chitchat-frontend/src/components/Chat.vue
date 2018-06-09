methods: {
  signUp () {
    $.post('http://localhost:8000/auth/users/create/', this.$data, (data) => {
      alert("Your account has been created. You will be signed in automatically")
      this.signIn()
    })
    .fail((response) => {
      alert(response.responseText)
    })
  },

  signIn () {
    const credentials = {username: this.username, password: this.password}

    $.post('http://localhost:8000/auth/token/create/', credentials, (data) => {
      sessionStorage.setItem('authToken', data.auth_token)
      sessionStorage.setItem('username', this.username)
      this.$router.push('/chats')
    })
    .fail((response) => {
      alert(response.responseText)
    })
  }
}
