<script setup>
    import { ref } from 'vue'

    import sidebarLayout from '@/components/sidebarLayout.vue'

    const logoPath = '/logo.webp'

    const sidebarItems = ref([
        {name: 'home', tooltip: 'Home', path: '/'},
        {name: 'analytics', tooltip: 'Analysis', path: '/analysis'},
        {name: 'settings', tooltip: 'Settings', path: '/settings'}
    ])
</script>

<template>
    <sidebarLayout :items="sidebarItems" :logo="logoPath" logoName="Cshub"/>
</template>

<style scoped>
</style>
