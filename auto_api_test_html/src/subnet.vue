<style scoped>
body {
  background-color: #333
  }
</style>
<style lang="less">
  .ivu-layout-sider-trigger{
    z-index: 1001 !important;
    height: 29px !important;
    top: 11% !important;
    line-height: 34px !important;
  }
  .ivu-layout-sider-zero-width-trigger{
    top:0vh !important;
  }
  .ivu-picker-panel-sidebar{
    width: 20% !important
  }
</style>
<template >
  <router-view ></router-view>
</template>
<script>
export default {
  name: 'Subnet'
}
</script>
