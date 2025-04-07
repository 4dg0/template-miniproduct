# Project Name: Template-SAAS

## Description

A template for a SaaS application

## TechStack

- UI & Frontend - Web PWA App with Ionic capacitor into android & ios:
  /web directory

  This module is responsible for the product site as well as client functionality. SSG/SPA (hydration) strategy is used, i.e. all front end logic is on the client, web module has no runtime on the server, static is distributed via nginx

  - tailwind v4
  - svelte 5
  - sveltekit
  - zod
  - bits.ui
  - capacitor
  - pocketbase (client for acess to Pocketbase SQLIte service)

- API (backend AI module):
  /api directory

  This module is responsible for custom server routers if they are needed (payment webhook and so on), as well as for interacting with external LLM and transcription providers. In general, this is the main backend, which does not belong to the generic functionality of pocketbase

  - FastAPI
  - pydantic
  - pocketbase (client for acess to Pocketbase SQLIte service)

## Main Features

## Support Features

1. Create personal profile and manage it
2. Pay for subscription online

## Project Structure

/api - Python FastAPI backend
/web - Frontend Sveltekit web-app
/scripts - some useful python scripts
/research - python scripts for experimenting with ai and working with data
