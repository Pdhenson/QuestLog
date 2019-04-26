
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: 'You loaded this page on  ' + new Date().toLocaleString()
  }
})

var app4 = new Vue({
  el: '#app-4',
  data: {
    Quests: [],
    seen:true,
    unseen:false

    },
    // Adapted from https://stackoverflow.com/questions/36572540
    created: function() {
      this.fetchQuestList();
      this.timer = setInterval(this.fetchQuestList, 10000);
    },

    methods:{
      fetchQuestList: function() {

        axios
        .get('/quests/')
        .then(response => (this.Quests = response.data.Quests))
      console.log(this.Quests)
      this.seen=false
      this.unseen=true
    },

    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  },

})
