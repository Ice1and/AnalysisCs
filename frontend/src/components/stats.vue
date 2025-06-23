<script setup>
    import { computed } from 'vue'

    const props = defineProps({
        title: {
            type: String,
            required: true
        },
        amount: {
            type: Number,
            required: true
        },
        rate: {
            type: Number,
            required: true
        }
    })

    const formattedRate = computed(() => {
        const value = (props.rate * 100).toFixed(1)
        return `${value}%`
    })
</script>

<template>
    <div>
        <div class="w-full border-t border-zinc-950/10"></div>
        <div class="mt-6 text-lg/6 font-medium sm:text-sm/6">{{ props.title }}</div>
        <div class="mt-3 text-3xl/8 font-semibold sm:text-2xl/8">{{ props.amount }}</div>
        <div class="mt-3 text-sm/6 sm:text-xs/6">
            <span class="inline-flex gap-x-1.5 px-1.5 py-0.5 text-sm/5 font-medium bg-lime-400/20 text-lime-700 rounded-md items-center sm:text-xs/5">{{ formattedRate }}</span>
            <span class="ml-1 text-zinc-500">from last day</span>
        </div>
    </div>
</template>

<style scoped>

</style>