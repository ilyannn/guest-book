<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Messages</h1>
        <hr><br>
        <alert :text=alertText :variant=alertVariant v-if="showAlert"/>
        <br>
        <form class="addForm" @submit.prevent="onAdd">
          <b-form-input v-model="newMessageAuthor" placeholder="Your name"/>
          <b-form-textarea v-model="newMessageText" placeholder="Your message"/>
          <b-button
            variant="success"
            @click="onAdd"
            class="w-100"
            :disabled="$v.newMessageAuthor.$invalid || $v.newMessageText.$invalid">
            Add
          </b-button>
        </form>
        <br>
        <form class="searchForm" @submit.prevent="onSearch">
          <b-input-group>
            <b-form-input type="search" v-model="searchQuery" placeholder="Search query"/>
            <b-button
              variant="primary"
              @click="onSearch">
            Search
            </b-button>
          </b-input-group>
        </form>
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
                <b-button
                  variant="danger"
                  @click="onDeleteMessage(message)">
                  Delete
                </b-button>
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
import { validationMixin } from 'vuelidate';
import { required } from 'vuelidate/lib/validators';
import Alert from './Alert.vue';

export default {
  mixins: [validationMixin],
  data() {
    return {
      messages: [],
      showAlert: false,
      alertText: '',
      alertVariant: '',
      newMessageAuthor: '',
      newMessageText: '',
      searchQuery: '',
    };
  },
  validations: {
    newMessageAuthor: {
      required,
    },
    newMessageText: {
      required,
    },
  },
  components: {
    alert: Alert,
  },
  methods: {
    getMessages() {
      this.showAlert = false;
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
    onAdd() {
      this.$v.newMessageAuthor.$touch();
      this.$v.newMessageText.$touch();
      if (this.$v.newMessageAuthor.$anyError || this.$v.newMessageText.$anyError) {
        return;
      }
      const path = 'http://localhost:5000/messages';
      axios.post(path, { author: this.newMessageAuthor, text: this.newMessageText })
        .then(() => {
          this.getMessages();
          this.newMessageText = '';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMessages();
          this.alertText = "Couldn't add the message";
          this.alertVariant = 'warning';
          this.showAlert = true;
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
