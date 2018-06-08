<template>
  <div class="container">
    <h1 class="text-center">Welcome to ChitChat!</h1>
    <div id="auth-containier" class="row">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link active" id="signup-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="true">Sign Up</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false">Sign In</a>
          </li>
        </ul>

        <div class="tab-content" id="myTabContent">

          <div class="tab-content" id="myTabContent">

            <div class="tab-pane fade aria-labelledby="signin-tab">
              <form @submit.prevent="signUp">
                <div class="form-group">
                  <input v-model="email" type="email" class="form-control" 
