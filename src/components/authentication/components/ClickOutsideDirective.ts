export default {
  beforeMount(el, binding) {
    console.log("binding",binding);
    console.log("el",el);
    el.clickOutsideEvent = function(event) {
      console.log("event",event);
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event);
      }
    };
    document.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent);
  },
};