<script setup>
    const props = defineProps({
        title: {
            type: String,
            required: true
        },
        value: {
            type: String,
            required: true
        },
        date: {
            type: String,
            required: true
        }
    })
</script>

<template>
    <div>
        <div class="w-full border-t border-zinc-950/10"></div>
        <div class="mt-6 text-lg/6 font-medium sm:text-sm/6">{{ props.title }}</div>
        <div class="mt-3 text-3xl/8 font-semibold sm:text-2xl/8">{{ props.value }}</div>
        <div class="mt-3 text-sm/6 sm:text-xs/6">
            <span class="inline-flex items-center rounded-md px-1.5 py-0.5 text-sm/5 font-medium sm:text-xs/5 bg-lime-400/20 text-lime-700 forced-colors:outline">0.0%</span>
            <span class="text-zinc-500"> from {{ props.date }}</span>
        </div>
    </div>
</template>

<style scoped>

</style>