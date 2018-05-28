var  vm = new Vue({
    el: '#vue_det',
    data: {
       company : "Stashing Words",
       
    },
    methods: {
       mydetails : function() {
          return "I am "+this.firstname +" "+ this.lastname;
       }
    }
 })