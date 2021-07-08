<template>
  <div>
    <h1>this is about page</h1>
    <!-- 자식이 보낸 child-input-change으로 정보를 입력받는다. -->
    <NewComponent my-message="this is prop data" @child-input-change="prarengGetChange"/>
  </div>
</template>

<script>
// import NewComponent from '../components/NewComponent.vue'
// @ === '/src'
import NewComponent from '@/components/NewComponent.vue'

export default {
  name: 'About',
  components: {
    NewComponent,
  },
  methods: {
    prarengGetChange: function (textInput) {
      console.log(`하위 컴포넌트 NewComponent로 부터 받은 ${textInput}이다.`)
    }
  },
}
</script>

<style>

</style>
