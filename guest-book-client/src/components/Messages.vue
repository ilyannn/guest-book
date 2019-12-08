<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Messages</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add</button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Time</th>
            <th scope="col">Author</th>
            <th scope="col">Message</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(message, index) in messages" :key="index">
            <td>{{ message.created_date }}</td>
            <td>{{ message.author_name }}</td>
            <td>{{ message.text }}</td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      messages: [],
    };
  },
  methods: {
    getMessages() {
      const path = 'http://localhost:5000/messages';
      axios.get(path)
        .then((res) => {
          this.messages = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.error(error);
        });
    },
  },
  created() {
    this.getMessages();
  },
};
</script>
