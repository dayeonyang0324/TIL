<template>
  <div id="app">
    <h2>App</h2>
    <input type="text" v-model="appData">
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>
    <!-- :가 붙은 정보는 자식에게 보내줄 data(:kebab-case ='camelCase') -->
    <Parent 
    :app-data="appData"
    :parent-data="parentData"
    :child-data="childData"
    @parent-input="onParentInput"
    @child-input="onChildInput"
    />
    <!-- @가 붙은 2개는 자식으로 부터 받아온 정보 -->
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'

export default {
  name: 'App',
  components: {
    Parent,
  },
  data: function () {
    return {
      appData: '',
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onParentInput: function (parentData) {
      this.parentData = parentData
    },
    onChildInput: function (childData) {
      this.childData = childData
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
