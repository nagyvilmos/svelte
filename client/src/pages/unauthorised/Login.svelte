<script>
  import { doRequest } from "../../api";
  import { auth } from "../../store";
  let name = "";
  let password = "";
  let valid = false;
  $: valid = !!name && !!password;

  let userSet = false;
  auth.subscribe((value) => {
    userSet = !!value.user;
  });

  const handleLogin = () => {
    console.log({ name, password });
    doRequest("auth/login", auth.login, auth.logout, {
      parameters: { name, password },
    });
  };

  /* type="email" */
</script>

<div class="login">
  <form on:submit|preventDefault={handleLogin}>
    {#if userSet}
      <p>Invalid credentials, please try again</p>
    {/if}
    <p>
      <input
        class="full-width"
        bind:value={name}
        placeholder="email address"
        autocomplete="current-email"
        required
      />
    </p>
    <p>
      <input
        class="full-width"
        bind:value={password}
        type="password"
        placeholder="password"
        autocomplete="current-password"
        required
      />
    </p>
    <p><button class="positive" disabled={!valid} type="submit">Login</button></p>
  </form>
  <p><a href="/forgotton">I have forgotton my password</a></p>
</div>

<style>
  .full-width {
    width: 100%;
  }
  .login {
    border: 2px solid;
    border-radius: 8px;
    margin-left: 35vw;
    margin-right: 35vw;
    padding: 4px;
  }
  input {
    border: 2px solid;
    border-radius: 8px;
    padding: 4px;
    background-color: var(--theme-background);
    color: var(--theme-color);
    border-color: var(--theme-color);
  }
</style>
