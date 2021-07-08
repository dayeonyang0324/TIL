<template>
  <div>
    <h2>New Component!</h2>
    <h2>{{ myMessage }}</h2>
    <input @keyup.enter="childInputChange" v-model="childInputData" type="text">
  </div>
</template>

<script>
export default {
  name: 'NewComponent',
  data: function () {
    return {
      // 이 components에서 작성될 data
      childInputData: '',
    }
  },
  // 부모에게서 받아온 data
  props: {
    myMessage: {
      type: String,
      required: true,
    },
  },
  methods: {
    childInputChange: function () {
      // 부모로 정보를 보낸다. 이름은 child-input-change
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>
