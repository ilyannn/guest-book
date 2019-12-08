<template>
  <div>
    <b-alert :variant=variant show>{{ text }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['text', 'variant'],
};
</script>
