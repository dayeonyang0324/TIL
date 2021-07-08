<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  // 부모(Home)에게서 상속받아오는 data
  props: {
    msg: String
  }
}
</script>

<!-- 이 components에만 style을 적용하고 싶다면 scoped를 사용한다. -->
<style scoped> 
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
