<template>
  <div class="modal">
    <div class="modal-content">
      <span class="close" @click="closeModal">&times;</span>

      <div v-if="step === 'friendsGroups'">
        <h2>Friends & Groups</h2>

        <div class="modal-body">
          <!-- Friends Section -->
          <div class="section friends">
            <h3>Friends</h3>
            <ul class="list">
              <li v-if="!friends.length" class="no-items">
                You have no friends! Billy No Mates. You are pathetic.
                <br/>&nbsp;
              </li>
              <li v-else v-for="friend in friends" :key="friend.friend_id" :id="friend.friend_id" class="list-item">
                {{ friend.friend_name }}
                <span :class="{'status-online': friend.isOnline, 'status-offline': !friend.isOnline}">
                  {{ friend.isOnline ? 'Online' : 'Offline' }}
                </span>
              </li>
            </ul>
            <button class="btn btn-custom btn-wide" @click="step = 'addFriend'">Add Friend</button>
          </div>
          <hr style="background-color: white; width: 100%; margin-bottom: 2rem"/>
          <!-- Groups Section -->
          <div class="section groups">
            <h3>Groups</h3>
            <ul class="list">
              <li v-for="group in groups" :key="group.id" class="list-item">
                {{ group.name }} ({{ group.activeMembers }} active) <a href="#">Join</a>
              </li>
            </ul>
            <button class="btn btn-custom btn-wide" @click="createGroup">Create Group</button>
          </div>
        </div>
      </div>

      <!-- Add Friend Step -->
      <div v-if="step === 'addFriend'">
        <h2>Add a Friend</h2>
        <div class="modal-body">
          <div>
            <div style="margin: 1rem 0">
              <input type="text" style="width: 100%; height: 2rem;" v-model="searchQuery" placeholder="Enter username" class="search-input" />
            </div>
            <button class="btn btn-custom btn-wide" @click="searchUser">Add Friend</button>
          </div>
         
          <div style="margin: 1rem 0;">
            <button class="btn btn-custom btn-wide" @click="step = 'friendsGroups'">Back</button>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      step: 'friendsGroups',
      searchQuery: '',
      searchResult: null, 
      groups: [
        { id: 1, name: 'Vue Enthusiasts', activeMembers: 5 },
        { id: 2, name: 'Open Source Developers', activeMembers: 8 },
      ],
    }
  },
  computed: {
    friends() {
      if (this.$store.state.friends === null) {
        return []
      }
      return this.$store.state.friends
    }
  },
  methods: {
    closeModal() {
      this.$emit('close');
    },
    searchUser() {

      const addFriendUrl = 
        `${this.$store.state.serverUrl}/friends/add/${this.searchQuery.trim()}/`

      axios.post(addFriendUrl).then(resp => {
        this.$store.commit('setFriendList', resp.data)
      }).catch((error) => {
        console.log(error)
      })
    },
    addFriend(user) {
      // Add the user to the friends list
      this.friends.push({
        id: user.id,
        name: user.name,
        isOnline: false, // Default to offline initially
      });
      
      // Reset search and go back to the friendsGroups view
      this.searchResult = null;
      this.searchQuery = '';
      this.step = 'friendsGroups';
    },
    createGroup() {

    }
  }
};
</script>

<style scoped>
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.modal-content {
  padding: 30px;
  border-radius: 8px;
  width: 500px;
  max-height: 90%;
  overflow-y: auto;
  background-color: #0000008c;
  border-color: rgba(255, 0, 0, 0.315);
  position: relative;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.close {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 24px;
  color: #ffffff;
  cursor: pointer;
}

.btn-wide {
  width: 100%;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.modal-body {
  display: flex;
  flex-direction: column;
}

.section {
  margin-bottom: 30px;
}

h3 {
  margin-bottom: 10px;
}

.list {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.list-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 10px;
  margin-bottom: 5px;
  background-color: #312e2e;
  border-radius: 5px;
}

.list-item:not(:last-child) {
  margin-bottom: 8px;
}

.status-online {
  color: green;
}

.status-offline {
  color: red;
}

.add-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  border: none;
  color: white;
  font-size: 14px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.add-button:hover {
  background-color: #0056b3;
}
</style>
