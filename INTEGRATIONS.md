# Boons integrations

Boons can be used from GitHub, distributed through Agensi, installed as local Agent Skills, or integrated into a custom agent. These routes are complementary.

## Agensi — recommended quick connection

[Open Boons on Agensi](https://www.agensi.io/skills/boons)

1. Create or sign in to an Agensi account.
2. Open the Boons skill listing.
3. Follow Agensi's current instructions to connect its MCP server to your AI client.
4. Complete the sign-in and authorization flow.
5. Ask the connected agent to find and use Boons for the task.

Agensi provides a convenient distribution and MCP access route. The host agent still determines available context, tools, workspace access, and execution permissions.

Agensi's current MCP documentation specifies:

- Remote MCP over Streamable HTTP.
- OAuth 2.1 authorization; no API keys.
- The default sign-in-first endpoint: `https://mcp.agensi.io/mcp/auth`.
- A `read` scope for browsing and an `install` scope for installing or purchasing skills, with user approval for purchases.
- One active agent connection per account: authorizing a new client can invalidate the previous client's connection.

Check the [Agensi MCP and sign-in documentation](https://www.agensi.io/docs/mcp-server) before setup; endpoints, supported clients, limits, and account behavior can change. Do not copy tokens into prompts, source files, screenshots, or Git.

### Which hosts?

Use Agensi directly with a client listed in its current connection guides. Chat interfaces are useful for conversational workflows when their MCP support is available. Codex and Claude Code are especially useful when the task also needs repository, terminal, or workspace access.

Other hosts, including DeepSeek-based clients, are supported only when the particular client exposes a compatible MCP connection and completes Agensi's authentication flow. Do not assume every product or interface with the same model name supports MCP.

## GitHub — open-source route

[Boons repository](https://github.com/FlowArchitect895/Boons)

Use GitHub when you want to inspect, fork, modify, pin, or self-manage the skill files. You can install selected folders with the Skills CLI or copy them into the assistant's documented skill directory. See [INSTALL.md](INSTALL.md).

Agensi is not required. The GitHub route remains available if you prefer manual installation or want to build your own integration.

## Codex and Claude Code

These workspace-connected agents are recommended for implementation work because they can operate on a project when the user grants the relevant access.

- [Codex MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)
- [Claude Code documentation](https://code.claude.com/docs)

Connect Agensi using the current client-specific instructions. Then verify the connection in the agent before relying on it. Keep repository permissions, terminal permissions, and external tool permissions scoped to the task.

## REA — optional specialist analysis

[REA upstream repository](https://github.com/morluto/rea)

REA is an independent reverse-engineering toolkit and MCP integration. It is optional; Boons' `rea-amplify` skill can also analyze user-supplied artifacts and available tool results without requiring REA.

The upstream REA repository documents setup with:

```sh
npx rea-agents setup
```

It supports several coding agents, including Claude Code and Codex. Review the proposed configuration changes before approving them, then restart the agent as instructed. Check REA's current README and installation guide for Node.js requirements, supported agents, optional analysis engines, and platform-specific dependencies.

The `rea-amplify` skill and REA software are separate projects:

- Boons provides the evidence-analysis workflow and downstream handoff.
- REA provides its own MCP tools and analysis capabilities.
- Ghidra, Hopper, IDA, and other analysis tools have their own installation, licensing, and compatibility requirements.

REA is not a guarantee against an agent's permission restrictions. Tool access remains subject to the host agent, operating system, configuration, and user approval.

## Local models and custom workspaces

A local model can use Boons instructions directly if the host application supplies them. To use Agensi, the local application must also implement a compatible MCP client and authentication flow.

For a custom workspace such as Odysseus, a coding agent can help implement and test the integration. Alternatively, developers can build their own adapter. Treat this as a software project: define the MCP client boundary, credential storage, tool schemas, error handling, permissions, and tests before connecting it to a model.

## Integration boundaries

- Connecting Agensi does not grant local filesystem or terminal access.
- Installing a skill does not install its optional tools.
- A model's capabilities do not establish that a particular client exposes those capabilities.
- Never claim an integration works until it has been connected and tested in the target environment.
- Review external projects and permissions independently; Boons does not maintain or guarantee third-party software.
