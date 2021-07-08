<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- 3. template에 지정하기(보내고 싶은 데이터를 보낼 수 있음) -->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// 자식을 지정하기 위한 3단계
// 1. import
// @ == /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  // 2. components 불러오기
  components: {
    HelloWorld
  }
}
</script>
