<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Messages</h1>
        <hr><br>
        <alert :text=alertText :variant=alertVariant v-if="showAlert"/>
        <br>
        <button type="button" class="btn btn-primary btn-sm">Add</button>
        <br>
        <form class="searchForm" @submit.prevent="onSearch">
          <input type="text" v-model="searchQuery" placeholder="Search query">
        </form>
        <button
          type="button"
          class="btn btn-secondary btn-sm"
          @click="onSearch">
          Search
        </button>
        <br>
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
            <td>{{ new Date(message.created_date).toLocaleTimeString() }}</td>
            <td>{{ message.author_name }}</td>
            <td>{{ message.text }}</td>
            <td>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="onDeleteMessage(message)">
                  Delete
                </button>
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
import Alert from './Alert.vue';

export default {
  data() {
    return {
      messages: [],
      showAlert: false,
      alertText: '',
      alertVariant: '',
      searchQuery: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getMessages() {
      const path = 'http://localhost:5000/messages';
      const query = {
        params: {
          search: this.searchQuery,
        },
      };
      axios.get(path, query)
        .then((res) => {
          this.messages = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.error(error);
        });
    },
    onSearch() {
      this.getMessages();
    },
    onDeleteMessage(message) {
      this.removeMessage(message.id);
    },
    removeMessage(messageID) {
      const path = `http://localhost:5000/messages/${messageID}`;
      axios.delete(path)
        .then(() => {
          this.getMessages();
          this.alertText = 'Message successfully removed';
          this.alertVariant = 'success';
          this.showAlert = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMessages();
          this.alertText = "Couldn't remove the message";
          this.alertVariant = 'warning';
          this.showAlert = true;
        });
    },
  },

  created() {
    this.getMessages();
  },
};
</script>
