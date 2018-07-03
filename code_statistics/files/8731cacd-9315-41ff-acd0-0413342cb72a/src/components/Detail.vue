<template>
  <div>
    <h1>课程详细页面</h1>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
      }
    },
    mounted(){
      console.log(this.$route.params.id)
    }
  }
</script>

<style scoped>

</style>
